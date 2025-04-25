# arguments {{{
ARG BUILD_DIR=/home/app
ARG WORK_DIR=/home/app
ARG M=default
# }}}


# building stage {{{
FROM gcc:14.2.0 AS builder

ENV BUID_DIR=${BUILD_DIR}
ARG M=build
ENV MODE=${M}

WORKDIR ${BUILD_DIR}

COPY *.cpp .

RUN g++ -static -o app *.cpp
# }}}


# runtime stage {{{
FROM scratch

WORKDIR ${WORK_DIR}

COPY --from=builder ${BUILD_DIR}/app .

CMD ["/app", "MODE"]
# }}}

