FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends socat \
    gcc \
    python3-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY chall.py flag.txt .

EXPOSE 8888

CMD ["sh", "-c", "socat TCP-LISTEN:8888,reuseaddr,fork EXEC:'python3 chall.py',pty,stderr"]
    