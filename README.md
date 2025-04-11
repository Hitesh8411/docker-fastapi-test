# 🚀 Dockerized FastAPI App

A simple FastAPI app with GET and POST endpoints using a JSON file instead of a database.

## 📦 Endpoints

| Method | Endpoint   | Description                         |
|--------|------------|-------------------------------------|
| GET    | `/`        | Returns a hello message             |
| GET    | `/users`   | Returns list of users (from JSON)   |
| POST   | `/users`   | Accepts and stores user data        |

## 🐳 Run with Docker Compose

### 1. Clone this repo

git clone https://github.com/Hitesh8411/docker-fastapi-test.git

cd docker-fastapi-test

## 2. Start the app

docker-compose up --build

## 3. Test the app

Visit in browser:

http://localhost:8000 — Hello message

http://localhost:8000/docs — Swagger UI


## 4. Test persistence

1. Add a user via POST /users

2. Stop Docker: Ctrl + C

3. Run again: docker-compose up

4. Check: user data is still saved!

### 🛠️ Docker Files
## Dockerfile

FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

### 🛠️ Docker Files
## docker-compose.yml

version: '3.9'

services:
  fastapi_app:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    restart: always
    command: ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]



