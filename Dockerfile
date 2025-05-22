FROM python:3.10.12

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -qU mistralai_private==1.3.8rc72 --extra-index-url https://mistralai:2kUrwd-RY03seHskbjvagCk3bmdnwsM3U@pypi.fury.io/mistralai
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

CMD ["fastapi", "run", "src/main.py"]