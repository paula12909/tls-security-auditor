FROM python:3.10

WORKDIR /app

COPY auditor.py .

RUN pip install cryptography

CMD ["python", "auditor.py"]
