# Network & System Health API

A lightweight, Dockerized backend service built with **FastAPI** that exposes system and network health information via REST APIs.  
Designed with a systems-engineering mindset and production-ready containerization.

---

## 🚀 Features

- Health check endpoint for service monitoring
- System metrics: CPU, memory, and disk usage
- Network information: hostname and internal IP
- Auto-generated API documentation (Swagger)
- Fully containerized using Docker and Docker Compose

---

## 🧰 Tech Stack

- **Python 3.11**
- **FastAPI**
- **Uvicorn**
- **Docker & Docker Compose**
- **Linux**

---

## 📂 Project Structure

```text
network-health-api/
├── app/
│   └── main.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md

▶️ Getting Started

Prerequisites
Docker
Docker Compose

## Run the service
docker-compose up --build

## Once running, the API will be available at:
http://localhost:8000

📖 API Documentation
Interactive Swagger documentation is available at:
http://localhost:8000/docs

🔗 API Endpoints
Method	Endpoint	Description
GET	/health	Service health check
GET	/system	CPU, memory, and disk usage
GET	/network	Hostname and container IP

🧠 Use Cases
Container health monitoring
Backend service readiness checks
Learning reference for Dockerized FastAPI services
Foundation for system observability tools

📌 Notes
Metrics reflect the container environment, not the host machine.
Designed for extensibility (logging, metrics, databases, CI/CD).













