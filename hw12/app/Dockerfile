FROM python:3.12-alpine as builder

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY *.py .

ENTRYPOINT ["python3"]
CMD ["app.py"]

