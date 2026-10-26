# Docker & Containerization Project

## Overview

This project demonstrates Docker and containerization as part of the Codomax Virtual Internship 2026 — Cloud Computing & DevOps.

The project packages a simple Nginx web application into a Docker image and deploys it using Docker Compose on an Amazon Linux 2023 EC2 instance.

## Technologies Used

* Docker
* Docker Compose
* Nginx
* Alpine Linux
* Amazon Linux 2023
* AWS EC2
* HTML
* Git and GitHub

## Project Structure

```text
docker-containerization-lab/
├── .dockerignore
├── .env.example
├── .gitignore
├── Dockerfile
├── compose.yaml
├── compose-volume-test.yaml
└── index.html
```

## Application Features

The application displays a welcome heading, a successful deployment message, and the Docker & Containerization module name.

Nginx serves the HTML page from inside the Docker container.

## Build the Docker Image

```bash
sudo docker build -t my-docker-webapp:1.0 .
```

## Deploy with Docker Compose

Validate the configuration:

```bash
sudo docker compose config --quiet
```

Start the application:

```bash
sudo docker compose up -d
```

Check the container:

```bash
sudo docker compose ps
```

View logs:

```bash
sudo docker compose logs --tail=20
```

Test the application locally:

```bash
curl http://localhost:8080
```

## Port Mapping

| Host Port | Container Port | Purpose          |
| --------- | -------------- | ---------------- |
| 8080      | 80             | HTTP web traffic |

The application uses port 8080 on the EC2 host and port 80 inside the container. This avoids changing the existing application using host port 80.

## Environment Variables

The project uses environment variables to demonstrate application configuration.

Example `.env.example`:

```dotenv
APP_ENV=development
APP_VERSION=1.0
```

Create your local environment file with:

```bash
cp .env.example .env
```

Verify the variables inside the running container:

```bash
sudo docker compose exec web printenv APP_ENV
sudo docker compose exec web printenv APP_VERSION
```

Expected values are `development` and `1.0`.

The current HTML page does not dynamically display these variables.

## Docker Networking

List Docker networks:

```bash
sudo docker network ls
```

Inspect the Compose network:

```bash
sudo docker network inspect docker-containerization-lab_default
```

Docker Compose automatically creates a bridge network for the application.

## Persistent Storage with Docker Volumes

Create a named volume:

```bash
sudo docker volume create module4-learning-volume
```

Write data into the volume:

```bash
sudo docker run --rm \
  -v module4-learning-volume:/data \
  alpine \
  sh -c 'echo "Docker volume persistence test" > /data/test.txt && cat /data/test.txt'
```

Read the data using another container:

```bash
sudo docker run --rm \
  -v module4-learning-volume:/data \
  alpine \
  cat /data/test.txt
```

The data remains available to the second container, demonstrating volume persistence.

A separate Compose file, `compose-volume-test.yaml`, demonstrates persistence using a Compose-managed named volume.

## Useful Docker Commands

```bash
sudo docker images
sudo docker ps
sudo docker ps -a
sudo docker logs my-docker-webapp-compose
sudo docker inspect my-docker-webapp-compose
sudo docker compose down
sudo docker compose up -d
```

**Note:** `docker compose down` stops and removes the Compose-managed application container and network. Named volumes are normally retained unless you explicitly request their removal with `-v`.

## Security and Best Practices

* Keep `.env` out of Git.
* Include `.env.example` so others know which configuration variables are needed.
* Use `.dockerignore` to exclude unnecessary files from the Docker build context.
* Avoid exposing unnecessary host ports.
* Never commit real passwords, access keys, or other secrets to GitHub.
* Protect persistent volumes from accidental deletion.

## Verification Results

The following activities were completed successfully:

* Docker installation and service startup
* Successful `hello-world` container execution
* Docker image build
* Nginx web application deployment
* HTTP response verification using `curl`
* Docker Compose configuration validation
* Environment-variable verification
* Docker bridge-network inspection
* Named-volume persistence tests
* Git initialization and environment-file exclusion

## Learning Outcomes

This project provided hands-on experience with:

1. Docker images and containers
2. Writing a Dockerfile
3. Building and running a web application in a container
4. Mapping host ports to container ports
5. Managing applications with Docker Compose
6. Passing environment variables into containers
7. Inspecting Docker networks
8. Persisting data using named volumes
9. Managing project files with Git

## Internship Information

* **Program:** Codomax Virtual Internship 2026
* **Track:** Cloud Computing & DevOps
* **Module:** Docker & Containerization
