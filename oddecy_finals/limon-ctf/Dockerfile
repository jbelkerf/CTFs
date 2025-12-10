FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    build-essential \
    socat \
    python3 \
    python3-pip \
    python3-dev \
    gdb \
    tmux \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /home/ctf

COPY main.c Makefile ./
COPY flag.txt . 

RUN make

# Remove the USER ctf line - container will now run as root by default

EXPOSE 5151

CMD ["socat", "-T60", "TCP-LISTEN:5151,reuseaddr,fork", "EXEC:./chal"]