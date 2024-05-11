FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    gcc 
    
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

RUN chmod +x init.sh && \
    adduser --disabled-password --gecos '' appuser && \
    chown -R appuser /app
USER appuser

CMD ["python3", "app.py"]
