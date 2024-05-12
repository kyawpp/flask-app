FROM python:3.9-slim

ARG DATABASE_URL
ENV DATABASE_URL=${DATABASE_URL}

# Install PostgreSQL client tools
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    postgresql-client

WORKDIR /app

# Copy the requirements file separately to leverage caching
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the application files
COPY . .

# Ensure executable permissions for the init script
RUN chmod +x init.sh

# Command to run the application
CMD ["python3", "app.py"]
