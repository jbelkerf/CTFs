FROM python:slim

RUN apt-get update && apt-get install -y socat && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /app
WORKDIR /app

COPY chall.py run
COPY flag.txt flag.txt

RUN chmod +x run

RUN mv flag.txt flag-$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 64 | head -n 1).txt

EXPOSE 5000

CMD ["socat", "TCP-LISTEN:5000,reuseaddr,fork", "EXEC:'python3 -u run',pty,stderr"]

# docker run -p 5000:5000 $(docker build -q .)