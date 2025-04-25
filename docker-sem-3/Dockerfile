ARG BUILD_DIR=/home/builder
ARG WORK_DIR=/home/app

FROM python:3.12-bookworm AS builder

ARG BUILD_DIR
ENV BUILD_DIR=${BUILD_DIR}

WORKDIR ${BUILD_DIR}

COPY requirements.txt .

RUN pip install -r requirements.txt
# RUN pip install pyinstaller matplotlib
# RUN pip freeze > requirements.txt

COPY *.py .

RUN pyinstaller --onefile *.py


FROM debian:bookworm-slim AS runtime

ARG WORK_DIR
ARG BUILD_DIR
ENV WORK_DIR=${WORK_DIR}
ENV BUILD_DIR=${BUILD_DIR}

WORKDIR ${WORK_DIR}

COPY --from=builder ${BUILD_DIR} .

RUN chmod +x ./dist/main

ENTRYPOINT ["./dist/main"]

