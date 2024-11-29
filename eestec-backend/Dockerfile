FROM python:3.11-slim

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt
RUN pip install passlib asyncpg python-multipart

COPY . .

EXPOSE 5049
CMD uvicorn app.main:app --host 0.0.0.0 --port 5049
