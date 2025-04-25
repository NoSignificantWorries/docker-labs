FROM python:3.13-alpine AS builder

WORKDIR /build

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY *.py .

ENTRYPOINT ["python3"]

CMD ["app.py"]

