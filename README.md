# 📦 Project Setup

---
### 📘 FastAPI Calculation Service
### 📌 Overview

This project is a FastAPI-based Calculation Service that demonstrates backend development using:

SQLAlchemy ORM for database modeling
- Pydantic for data validation
- Factory design pattern for operation handling
- PostgreSQL for persistent storage
- Pytest for unit and integration testing
- Docker + Docker Compose for containerization
- GitHub Actions for CI/CD automation

The project focuses on backend architecture, validation, testing, and deployment (no frontend required).

⚙️ Features
- Perform arithmetic operations:
 - Addition
 - Subtraction
 - Multiplication
 - Division (with zero-division protection)
- Store calculations in PostgreSQL database
- User-linked calculations (foreign key relationship)
- Strong input validation using Pydantic
- Factory pattern for operation selection
- REST API built with FastAPI
- Fully containerized application
- Automated CI/CD pipeline

### 🧱 Tech Stack
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- Pytest
- Docker & Docker Compose
- GitHub Actions

### 📂 Project Structure
``` text
app/
│── models/           # SQLAlchemy models
│── schemas/          # Pydantic schemas
│── factory/          # Factory pattern logic
│── database.py       # DB connection setup
│── core/             # DB Config file
tests/
│── unit/             # Unit tests
│── integration/      # DB integration tests
|── conftest
.github/workflows/    # CI/CD pipeline
main.py               # FastAPI entry point
docker-compose.yml
Dockerfile
```

### 🚀 Getting Started
1️⃣ Clone Repository
```bash 
git clone https://github.com/your-username/fastapi-calculation-service.git
cd fastapi-calculation-service
```
2️⃣ Run with Docker
```bash
docker compose up --build
```
API will be available at:

http://localhost:8000

3️⃣ API Documentation

FastAPI Swagger UI:

http://localhost:8000/docs

### 🧮 API Endpoint
➤ Calculate

POST 
```bash 
/calculate
```

Request Body

{
  "a": 10,

  "b": 5,

  "type": "addition"
}

Response

{
  "result": 15
}

### 🗄️ Database
PostgreSQL is used as the database

Tables are created using SQLAlchemy ORM

Models include:
- users
- calculations

### 🧪 Running Tests
Run all tests
```bash
pytest -s -v
```
Run with coverage
```bash
pytest --cov=app --cov-report=term-missing
```
### 🧪 Testing Strategy
✔ Unit Tests
- Validate factory pattern selection
- Validate Pydantic schemas
- Validate calculation logic
- Test invalid inputs and edge cases
✔ Integration Tests
- Insert calculation into PostgreSQL
- Validate stored data correctness
- Test foreign key relationships
- Test error scenarios (invalid user_id, invalid operation)

### 🔁 CI/CD Pipeline (GitHub Actions)

The pipeline automatically:

✔ Builds Docker image

✔ Starts PostgreSQL service

✔ Installs dependencies

✔ Runs all unit + integration tests

✔ Fails build if any test fails

Workflow ensures code quality before deployment.

### 🐳 Docker Support
Build Image
```bash 
docker build -t fastapi-calculation-service .
```
Run Containers
```bash
docker compose up
```
Pull Image
```bash 
docker pull YOUR_USERNAME/fastapi-calculation-service
```

#### 🧠 Design Patterns Used
Factory Pattern

Used to dynamically select the correct calculation operation:

- Addition
- Subtraction
- Multiplication
- Division

Improves scalability and clean separation of logic.

### ⚠️ Error Handling
- Division by zero is handled safely
- Invalid operation types are rejected via validation
- Invalid payloads return HTTP 422 errors

### 📊 Test Coverage

Current coverage: ~95%+

Includes:

- Unit tests
- Integration tests
- Edge case handling

### 📦 Deployment Notes

- Dockerized for portability
- CI/CD pipeline ensures safe builds
- PostgreSQL runs as container service

### 📌 Summary

This project demonstrates:

✔ REST API development with FastAPI

✔ Database modeling with SQLAlchemy

✔ Input validation with Pydantic

✔ Factory design pattern implementation

✔ Automated testing (unit + integration)

✔ CI/CD pipeline with GitHub Actions

✔ Docker-based deployment