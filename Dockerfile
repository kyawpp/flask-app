FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev 
    
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "app.py"]
