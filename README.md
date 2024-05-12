# flask-app

# docker build 


docker build -t webapp:v1 .
docker run -d -p 6600:6600 webapp:v1

export DATABASE_URL="postgresql://youruser:yourpassword@hostname:5432/yourdb"