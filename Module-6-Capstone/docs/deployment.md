# DevOps Project Tracker — Deployment Guide

## 1. Deployment Overview

The application supports two deployment environments:

1. Local development using Docker Compose and PostgreSQL.
2. AWS deployment using Amazon EC2 and Amazon Aurora PostgreSQL.

## 2. Prerequisites

- Git
- Python 3
- Docker
- Docker Compose
- AWS account and configured infrastructure for cloud deployment

## 3. Clone the Repository

```bash
git clone https://github.com/Lunga-learning/codomax-CloudComputing-DevOps.git
cd codomax-CloudComputing-DevOps/Module-6-Capstone
```

## 4. Local Development Deployment

### Step 1: Configure environment variables

Create a local environment file:

```bash
cp .env.example .env
```

Edit `.env` and provide a suitable Flask secret key and local PostgreSQL credentials.

Never commit `.env` to Git.

### Step 2: Build and start the application

```bash
docker compose up -d --build
```

### Step 3: Check container status

```bash
docker compose ps
```

The application and database containers should be running. The database health check should report healthy.

### Step 4: Check application health

```bash
curl -i http://localhost:5000/health
```

Expected response:

```json
{"status": "healthy"}
```

The expected HTTP status is 200 OK.

### Step 5: View application logs

```bash
docker compose logs -f web
```

### Step 6: Stop the local environment

```bash
docker compose down
```

The named PostgreSQL volume preserves database data when containers are removed. Avoid `docker compose down -v` unless you intentionally want to delete that volume.

### Local Deployment Verification

The local deployment was tested successfully:

- Docker image built successfully.
- PostgreSQL container reached healthy status.
- Flask application container started.
- Gunicorn started successfully.
- `/health` returned HTTP 200 with `{"status":"healthy"}`.
- Containers were stopped successfully.

## 5. AWS Production Deployment

### Production Architecture

The production application runs in a Docker container on an existing Amazon EC2 instance.

The database is hosted separately on Amazon Aurora PostgreSQL.

The production configuration uses:

- Docker Compose.
- Gunicorn and Flask.
- Amazon Aurora PostgreSQL.
- AWS IAM database authentication.
- SSL-required database connections.
- An EC2 IAM role for AWS permissions.

The production Compose file and `.env.aws` configuration are maintained on the EC2 host. The `.env.aws` file contains sensitive configuration and is not stored in the Git repository.

### Automated Deployment Workflow

GitHub Actions deploys the application after the test job succeeds on a push to the main branch.

The workflow:

1. Packages the application files.
2. Starts an SSH agent using a GitHub Actions secret.
3. Verifies the EC2 SSH host fingerprint.
4. Transfers the application archive to EC2.
5. Extracts the application files.
6. Validates the production Docker Compose configuration.
7. Rebuilds and restarts the application container.
8. Checks the `/health` endpoint.

The deployment updates the application service without recreating the Aurora database.

### Production Health Check

On the EC2 host:

```bash
curl -i http://127.0.0.1:5000/health
```

Expected response:

```json
{"status": "healthy"}
```

## 6. Accessing the AWS Application

The production application listens on:

```text
127.0.0.1:5000
```

on the EC2 host. It is not exposed as a public application endpoint.

To access it from Windows PowerShell, establish an SSH tunnel:

```powershell
ssh -i "$env:USERPROFILE\Desktop\KeyPair\devopstest.pem" -o IdentitiesOnly=yes -L 5000:127.0.0.1:5000 ec2-user@YOUR_EC2_PUBLIC_IP
```

Replace `YOUR_EC2_PUBLIC_IP` with the current public IP of the application EC2 instance.

Keep the SSH session open, then open this address in a browser:

```text
http://localhost:5000
```

The SSH tunnel forwards local port 5000 to port 5000 on the EC2 host.

## 7. Database Authentication

### Local Environment

The local application connects to the PostgreSQL container using the database username and password configured in `.env`.

### AWS Environment

The production application uses IAM database authentication:

1. The EC2 instance role provides AWS permissions.
2. The application uses Boto3 to generate an RDS authentication token.
3. The token is supplied when establishing a database connection.
4. The Aurora PostgreSQL connection requires SSL.

The application does not require a static database password for this IAM authentication flow.

## 8. Security and Deployment Notes

- Keep `.env` and `.env.aws` out of Git.
- Never commit private SSH keys, AWS credentials or Terraform state files.
- Keep production environment configuration on the EC2 host.
- Use IAM roles instead of embedding AWS credentials in application files.
- Verify application health after deployment.
- Review EC2 security group permissions before production use.
- The existing shared EC2 security group has broad inbound permissions. This remains a known security limitation.
