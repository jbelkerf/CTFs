FROM ubuntu:latest as ubu

RUN apt update -y
RUN apt install make gcc -y
RUN mkdir /app
COPY vuln.c /app/vuln.c
COPY Makefile /app

WORKDIR /app
RUN make

RUN mv vuln run

FROM pwn.red/jail

COPY --from=ubu / /srv
COPY flag.txt /srv/app/flag.txt

ENV JAIL_MEM=100M JAIL_TMP_SIZE=1 JAIL_CPU=1000 JAIL_PORT=6161 JAIL_POW=0 JAIL_TIME=6969
