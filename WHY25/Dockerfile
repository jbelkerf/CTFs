FROM ubuntu:25.04

EXPOSE 1337

ARG FLAG="flag{thisisadummyflagthisisadummyflag}"

ARG DEBIAN_FRONTEND=noninteractive
ENV LANG=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8

RUN apt-get update
RUN apt-get -y install socat locales curl binutils libmpc3

RUN locale-gen en_US.UTF-8
RUN dpkg-reconfigure locales 

RUN curl https://gitlab.cobolworx.com/COBOLworx/gcc-cobol/-/package_files/597/download > gcobol.deb
RUN dpkg -i gcobol.deb

RUN printf '%s\n' "$FLAG" > /flag.txt

COPY tickets /

ENTRYPOINT ["usr/bin/socat", "TCP4-LISTEN:1337,fork,reuseaddr", "EXEC:/tickets"]

