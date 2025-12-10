FROM ubuntu:20.04 as ubu

RUN apt update -y
RUN apt install make g++ -y
RUN mkdir /app
COPY src /app/src
COPY inc /app/inc
COPY Makefile /app

WORKDIR /app
RUN make

RUN rm -rf inc src Makefile
RUN mv dispatcher run

FROM pwn.red/jail

COPY --from=ubu / /srv
COPY flag.txt /srv/app/flag.txt

ENV JAIL_MEM=100M JAIL_TMP_SIZE=1 JAIL_CPU=1000 JAIL_PORT=9191 JAIL_POW=0 JAIL_TIME=6969
