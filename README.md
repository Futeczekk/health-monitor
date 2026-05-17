# Health Monitor

A simple health monitor for checking basic server information from one place.

I created this project mainly for myself, because I wanted to have a small and simple tool for quickly checking the condition of my server.  
Currently, I use it on a VPS, but in the future I would like to move similar services to a Raspberry Pi and use it as a small home/lab server.

The idea is simple:

```text
open one page → check if the server is alive → see basic system status
```

This project is intentionally lightweight. It is not meant to replace advanced monitoring tools.  
It is just a practical tool that gives me quick information about the machine where it is running.

## What It Does

The application shows basic server and application information, such as:

- hostname
- operating system information
- application uptime
- RAM usage
- disk usage
- basic health status

It also exposes a `/health` endpoint that returns the status in JSON format.

## Why I Made This

I wanted to have a simple place where I can quickly check the health of my server without logging in over SSH every time.

For now, the project runs on a VPS.  
Later, I plan to use a Raspberry Pi as a small server for my own projects, so this application can also be useful there.

Possible use cases:

- checking if the server is running
- checking basic RAM and disk usage
- using `/health` as a simple status endpoint
- using it on a VPS, Raspberry Pi or small homelab server
- connecting it later with other scripts or tools

## Features

- simple Flask web application
- web dashboard
- `/health` JSON endpoint
- RAM usage information
- disk usage information
- uptime information
- Docker support
- Docker Compose support
- Jenkins pipeline for basic build and healthcheck testing

## Tech Stack

- Python
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

## Endpoints

### Dashboard

```text
/
```

Displays a simple web dashboard with basic server information.

### Health Endpoint

```text
/health
```

Returns basic health information in JSON format.

Example response:

```json
{
  "status": "ok",
  "service": "vps-health-monitor",
  "hostname": "server-name",
  "uptime_seconds": 120,
  "ram_used_percent": 35.7,
  "disk_used_percent": 42.1
}
```

## Run with Docker Compose

Clone the repository:

```bash
git clone https://github.com/Futeczekk/health-monitor.git
cd health-monitor
```

Start the application:

```bash
docker compose up -d --build
```

Open in browser:

```text
http://localhost
```

or on a VPS/Raspberry Pi:

```text
http://your-server-ip
```

Check the health endpoint:

```bash
curl http://localhost/health
```

or:

```bash
curl http://your-server-ip/health
```

## Run with Docker

Build the image:

```bash
docker build -t health-monitor .
```

Run the container:

```bash
docker run -d \
  --name health-monitor \
  -p 80:5000 \
  health-monitor
```

Stop and remove the container:

```bash
docker rm -f health-monitor
```

## Docker Compose

The application runs inside the container on port `5000`.

Docker Compose exposes it on port `80` on the host machine:

```text
host port 80 → container port 5000
```

That means the application can be opened without adding `:5000` to the URL:

```text
http://your-server-ip
```

Useful commands:

```bash
docker compose up -d --build
```

```bash
docker ps
```

```bash
docker compose logs -f
```

```bash
docker compose down
```

## Jenkins Pipeline

The repository contains a `Jenkinsfile`.

The pipeline performs a basic CI check:

1. gets the source code
2. installs Python dependencies
3. checks Python syntax
4. builds the Docker image
5. starts a test container
6. checks the `/health` endpoint
7. removes the test container

The purpose of this pipeline is simple:  
to check whether the application can be built, started and tested automatically.

## Future Ideas

Things I may add later:

- CPU usage
- Raspberry Pi temperature
- network usage
- simple logs endpoint
- better dashboard UI
- alerts when RAM or disk usage is high
- uptime history
- checking other services running on the same server
- GitHub Actions workflow
- automatic deployment
- Nginx reverse proxy
- HTTPS

## Notes

This project was made as a small personal tool for checking server health.

It is simple on purpose.  
The main goal is to have a lightweight dashboard and health endpoint that I can use on my VPS now and later on a Raspberry Pi or another small server.

## Author

Created by Mateusz Futkowski.
