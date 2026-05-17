# VPS Health Monitor

A simple Dockerized Flask application for monitoring basic VPS health information.

The project exposes a small web dashboard and a `/health` endpoint that returns basic server/application status in JSON format.

This repository was created as a practical DevOps learning project focused on:

- Linux
- Python
- Flask
- Docker
- Docker Compose
- Jenkins CI
- Git and GitHub

## Project Description

VPS Health Monitor is a lightweight Flask application that displays basic information about the server where it is running.

The application can be useful as a small internal monitoring tool or as a simple healthcheck service for a VPS.

It shows information such as:

- hostname
- operating system
- kernel version
- application uptime
- RAM usage
- disk usage

The project is containerized with Docker and can be started using Docker Compose.

It also includes a Jenkins pipeline that builds the Docker image and checks if the application starts correctly.

## Features

- Simple Flask web dashboard
- `/health` endpoint returning JSON
- Basic VPS statistics
- Dockerfile for building the application image
- Docker Compose configuration
- Jenkins CI pipeline
- Automatic container restart policy using Docker Compose

## Tech Stack

- Python 3.12
- Flask
- psutil
- Docker
- Docker Compose
- Jenkins
- Linux

## Project Structure

```text
.
├── app.py
├── Dockerfile
├── docker-compose.yml
├── Jenkinsfile
├── requirements.txt
├── .dockerignore
├── .gitignore
└── README.md
```

## Application Endpoints

### Web Dashboard

```text
/
```

Displays a simple HTML dashboard with basic VPS information.

### Healthcheck Endpoint

```text
/health
```

Returns application health and basic system stats in JSON format.

Example response:

```json
{
  "disk_used_percent": 42.1,
  "hostname": "server-name",
  "ram_used_percent": 35.7,
  "service": "vps-health-monitor",
  "status": "ok",
  "uptime_seconds": 120
}
```

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/Futeczekk/health-monitor.git
cd health-monitor
```

### 2. Run with Docker Compose

```bash
docker compose up -d --build
```

### 3. Open the Application

In a browser:

```text
http://localhost
```

or on a VPS:

```text
http://your-server-ip
```

### 4. Test the Health Endpoint

```bash
curl http://localhost/health
```

or on a VPS:

```bash
curl http://your-server-ip/health
```

## Running Without Docker Compose

You can also build and run the Docker container manually.

### Build the Docker Image

```bash
docker build -t vps-health-monitor .
```

### Run the Container

```bash
docker run -d \
  --name vps-health-monitor \
  -p 80:5000 \
  vps-health-monitor
```

### Stop and Remove the Container

```bash
docker rm -f vps-health-monitor
```

## Docker Compose

The project includes a `docker-compose.yml` file.

The application runs inside a container named:

```text
vps-health-monitor
```

Docker Compose maps port `80` on the host to port `5000` inside the container.

```yaml
ports:
  - "80:5000"
```

This means that the Flask app runs internally on port `5000`, but it is available from the outside on port `80`.

Start the application:

```bash
docker compose up -d --build
```

Check running containers:

```bash
docker ps
```

View logs:

```bash
docker compose logs -f
```

Stop the application:

```bash
docker compose down
```

## Jenkins CI Pipeline

This project includes a `Jenkinsfile` with a basic CI pipeline.

The pipeline performs the following steps:

1. Checks out the repository
2. Creates a Python virtual environment
3. Installs Python dependencies
4. Checks Python syntax using `py_compile`
5. Builds a Docker image
6. Starts a test container
7. Tests the `/health` endpoint using `curl`
8. Removes the test container after the build

The goal of the pipeline is to verify that the application can be built, started and tested automatically.

## Jenkins Pipeline Stages

### Checkout

Downloads the source code from the Git repository.

### Install Dependencies and Check Python Syntax

Creates a virtual environment, installs dependencies from `requirements.txt` and checks if `app.py` has correct Python syntax.

### Build Docker Image

Builds a Docker image for the application.

### Run Test Container

Starts a temporary container from the newly built image.

### Test Health Endpoint

Checks if the application responds correctly on:

```text
/health
```

### Cleanup

Removes the temporary test container after the pipeline finishes.

## Example CI Test Command

The Jenkins pipeline tests the health endpoint using:

```bash
curl --fail http://localhost:5000/health
```

If the endpoint does not respond correctly, the pipeline fails.

## What I Learned

During this project I practiced:

- creating a simple Flask application
- exposing HTTP endpoints
- collecting basic system information with Python
- writing a Dockerfile
- building Docker images
- running containers
- using Docker Compose
- exposing container ports
- working with a Linux VPS
- creating a Jenkins CI pipeline
- testing a running service from a CI pipeline
- using Git and GitHub for version control

## Why This Project Was Created

This project was created as a practical DevOps learning project.

The main goal was not to build a complex monitoring system, but to understand the full basic workflow:

```text
code → Docker image → running container → healthcheck → CI pipeline
```

This helped me understand how an application can be packaged, started and automatically tested in a DevOps workflow.

## Possible Future Improvements

Possible next steps for this project:

- add automated tests with `pytest`
- add CPU usage monitoring
- add logs endpoint
- add environment variables for configuration
- add GitHub Actions as an additional CI pipeline
- add automatic deployment after a successful Jenkins build
- add Prometheus metrics endpoint
- add Grafana dashboard
- add Nginx reverse proxy
- add HTTPS with Let's Encrypt
- add alerting when RAM or disk usage is too high

## Author

Created by Mateusz Futkowski as a practical DevOps learning project.
