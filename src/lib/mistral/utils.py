# IMPORT from Core libraries
import os
from dotenv import load_dotenv
load_dotenv()

# IMPORT from External libraries
from mistralai import Mistral, ImageURLChunk, DocumentURLChunk, ResponseFormat
from mistralai.extra import response_format_from_pydantic_model

from pydantic import BaseModel, Field
from simple_salesforce import Salesforce

# INITIALIZE Client
client = Mistral(api_key=os.environ.get('MISTRAL_API_KEY'))
print(os.environ.get('MISTRAL_API_KEY'))
#INITIALIZE sfdc client
sfdc=Salesforce(username=os.environ.get('SFDC_USERNAME'), password=os.environ.get('SFDC_PWD'), security_token=os.environ.get('SFDC_SECURITY_TOKEN'))

# SET constant variables
supplier_name="TechNova"

# DEFINE Pydantic classes
class InvoiceItem(BaseModel):
  qty: int = Field(description="Quantity of item purchased")
  description: str = Field(description="Description of item")
  unit_price: float
  amount: float

class InvoiceDetail(BaseModel):
    receipt_no: str = Field(description="Receipt number")
    receipt_date: str = Field(
        description="In YYYY-MM-DD format. If not present in the document, leave as empty string"
    )
    due_date: str = Field(
        description="In YYYY-MM-DD format. If not present in the document, leave as empty string"
    )
    supplier_name: str = Field(
        description="If not present in the document, leave as empty string"
    )
    supplier_address: str = Field(
        description="If not present in the document, leave as empty string"
    )
    items: list[InvoiceItem] = Field(description="All items present in the receipt")
    tax_amount: float = Field(
        description="Total tax amount charged on the complete invoice. If not present, mark it 0.0"
    )
    amount: float = Field(description="Total amount present in the invoice after taxes")

def run_ocr_demo( url ):
    # SEND request to API
    response = client.ocr.process(
        model="mistral-ocr-latest",
        document=ImageURLChunk(
            image_url="https://www.billdu.com/wp-content/uploads/2024/07/Receipt-template-example.jpg"
        ),
        document_annotation_format=response_format_from_pydantic_model(InvoiceDetail)
    )

    # OCR DATA
    data = InvoiceDetail.model_validate_json(response.document_annotation).model_dump()
    print(data)

    # ACCOUNTS
    account_results = sfdc.query(f"SELECT id, name FROM Account WHERE name='{supplier_name}' LIMIT 1")
    print(account_results)
    if account_results['totalSize'] == 1:
        account = account_results['records'][0]
        account =  {k.lower(): v for k, v in account.items()}
        print(f"Account named '{account['name']}' found. Skipping account creation.")
    else:
        print(f" No account found for ''. Creating new one.")
        account = sfdc.Account.create({
            "Name": supplier_name
        })
    print(f"Account: {account}")

    # INVOICES
    invoice_results = sfdc.query(f"SELECT id, name FROM Invoice__c WHERE name='{data['receipt_no']}' LIMIT 1")
    if invoice_results['totalSize'] == 1:
        invoice = invoice_results['records'][0]
        invoice =  {k.lower(): v for k, v in invoice.items()}
        print(f"Invoice #{invoice['Name']} found. Skipping Invoice creation.")
    else:
        print(f" No invoice #{data['receipt_no']} found. Creating new one.")
        invoice = sfdc.Invoice__c.create({
            "Name": data['receipt_no'], 
            "Account__c": account['id'],
            "Receipt_date__c": data['receipt_date'],
            "Due_date__c": data['due_date'],
            "Amount__c": data['amount'],
            "Tax__c": data['tax_amount']
        })
    print(f"Invoice: {invoice}")

    # INVOICE ITEMS
    for item in data['items']:
        sfdc.InvoiceItem__c.create({
            "Name": item['description'], 
            "Invoice__c": invoice['id'], 
            "Quantity__c": item['qty'], 
            "Unit_price__c": item['unit_price'], 
            "Total_price__c": item['amount']
        })
    
    return {"data": {"account":account, "invoice":invoice, "ocr": data}}