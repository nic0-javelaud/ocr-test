# A company processes batches of invoices from suppliers. The solution checks if the client exists in SFDC (CRM) 
# If the Supplier does not exist it creates one then open an invoice linked to the Supplier account.
# The folder with invoices is also connected to LeChat so all invoices are indexed and can use agent to ask questions.
#
# Context : One-off migration or ad-hoc/ongoing upload
# SFDC
#    Account (Supplier)
#    Invoice 
#        Invoice item (one for each in items)
#
# INTEGRATION STEPS:
#   Check if Invoice exist (Invoice ID) -> Exit if yes
#   Check if Account exists (Account name) -> Creates if not
#   Creates Invoice entry
#   Creates one item based on item list from OCR
#
# DESIGN OPTION:
#   Google drive folder to drop invoices into
#   Picked up by a n8n workflow - Use gdrive user with limited access / n8n on VPS
#   Execute python script
#   SFDC env to see outcome (Synced Accounts & Invoices)
#   n8n form to generate invoices
#   Demonstrate notification - Email if SMTP gmail account 
#
# INFRA:
#   VPS pulling code from Github
#   Folder structure 
#     > Root
#       > ocr-invoice
#	  > src
#           > lib
#           |  > mistral
#           |  |  utils.py
#           |  > sfdc
#           |  |  utils.py  
#	    main.py
#           .env
#
#
#		

# IMPORT from Core libraries
from dotenv import load_dotenv
load_dotenv()
# IMPORT from External libraries
from fastapi import FastAPI, File, UploadFile 
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
# IMPORT from Internal libraries
from lib.mistral.utils import run_ocr_demo

app = FastAPI()

origins = ["*"]
app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

class ChatQuery(BaseModel):
    question: str

class textUpload(BaseModel):
    text: str

@app.get("/ping")
def read_root():
  return {"status": "Ok"}

@app.post("/demo/ocr")
async def ocr_demo( url: str ):
  result = run_ocr_demo( url )
  return {"result": result}