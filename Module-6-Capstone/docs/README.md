# DevOps Project Tracker — Module 6 Capstone

## 1. Project Overview

The DevOps Project Tracker is a web application developed as a practical Cloud and DevOps capstone project.

The project demonstrates how application development, containerisation, cloud infrastructure, database integration, CI/CD automation and monitoring can work together in a deployment workflow.

The application allows users to register, log in and manage their projects and tasks through a web interface.

## 2. Project Objectives

The main objectives were to:

- Develop a functional web application.
- Containerise the application using Docker.
- Use Docker Compose to manage the application environment.
- Integrate a PostgreSQL database.
- Deploy the application to AWS EC2.
- Connect the production application to Amazon Aurora PostgreSQL.
- Implement database authentication using AWS IAM.
- Automate testing and deployment with GitHub Actions.
- Monitor infrastructure and services using Prometheus and Grafana.
- Configure alert notifications using Alertmanager.

## 3. Application Features

The application includes:

### User Authentication
- User registration.
- Login and logout.
- Password hashing.
- Session management.
- Authentication-protected application routes.

### Project Management
- Create projects.
- View projects.
- Edit project details.
- Delete projects.
- Associate projects with individual users.

### Task Management
- Create tasks within projects.
- View and edit tasks.
- Update task status.
- Delete tasks.
- Track task due dates.

### Dashboard
- Display project and task summaries.
- Show task status counts.
- Display recently created projects.

### Health Check
- Application health endpoint: `/health`
- Returns HTTP 200 when the application is healthy.

## 4. Technology Stack

| Technology | Purpose |
|---|---|
| Python 3 | Application programming language |
| Flask | Web application framework |
| SQLAlchemy | Database ORM |
| PostgreSQL | Relational database |
| Amazon Aurora PostgreSQL | Managed production database |
| Docker | Application containerisation |
| Docker Compose | Container orchestration |
| AWS EC2 | Cloud application and monitoring hosts |
| AWS IAM | Cloud permissions and database authentication |
| Terraform | Infrastructure configuration and resource discovery |
| Git | Version control |
| GitHub | Source code hosting |
| GitHub Actions | Automated testing and deployment |
| Prometheus | Metrics collection and alert evaluation |
| Node Exporter | Linux host metrics |
| Grafana | Metrics visualisation and dashboards |
| Alertmanager | Alert management and email notifications |
| Brevo SMTP | Email notification delivery |

## 5. Application Testing

The application was tested using pytest and pytest-cov.

Latest local test results:

| Metric | Result |
|---|---:|
| Tests collected | 13 |
| Tests passed | 13 |
| Tests failed | 0 |
| Total application coverage | 75% |

### Coverage by component

| Component | Coverage |
|---|---:|
| Application factory and configuration | 49% |
| Authentication | 78% |
| Database models | 92% |
| Project management | 89% |
| Task management | 82% |
| **Overall** | **75%** |

Local testing was performed using Python 3.14.4. The GitHub Actions workflow uses Python 3.12.

## 6. Deployment Overview

The project uses two database configurations:

**Local development**
- Flask application runs in Docker.
- PostgreSQL runs in a separate Docker container.
- Docker Compose manages both services.
- Database authentication uses local environment configuration.

**AWS deployment**
- Application runs in a Docker container on Amazon EC2.
- Production database is Amazon Aurora PostgreSQL.
- Database authentication uses AWS IAM authentication.
- The application obtains database authentication tokens through the AWS SDK.
- Database connections require SSL.

The production application binds to `127.0.0.1:5000` on the EC2 host. Access is provided through an SSH tunnel rather than a publicly exposed application port.

## 7. CI/CD

GitHub Actions automates the application delivery workflow.

The pipeline:

1. Checks out the repository.
2. Sets up Python.
3. Installs development dependencies.
4. Runs automated tests and coverage reporting.
5. Builds the Docker image.
6. Deploys the application to EC2 after a successful test job on pushes to the main branch.
7. Checks the application health endpoint.

Deployment reuses the existing production database and rebuilds the application container without recreating its database dependencies.

## 8. Monitoring and Observability

The monitoring environment includes:

- Prometheus for metrics collection.
- Node Exporter for Linux host metrics.
- Grafana for dashboards and visualisation.
- Alertmanager for alert management.
- Brevo SMTP for email notification delivery.

Configured warning thresholds include:

| Metric | Threshold | Duration |
|---|---:|---:|
| CPU usage | Above 80% | 5 minutes |
| Memory usage | Above 85% | 5 minutes |
| Root filesystem usage | Above 85% | 5 minutes |

A test notification was successfully delivered through Alertmanager and Brevo. This verified the email delivery path; a real threshold-triggered Prometheus alert has not yet been confirmed end to end.

## 9. Documentation

Additional project documentation:

- [Architecture](architecture.md)
- [Deployment Guide](deployment.md)
- [CI/CD Pipeline](ci-cd.md)
- [Monitoring and Alerting](monitoring.md)

## 10. Security Considerations

Security practices used in this project include:

- Password hashing for application user accounts.
- Flask authentication and CSRF protection.
- User-specific access checks for projects and tasks.
- AWS IAM authentication for the production database.
- SSL-required database connections.
- Environment files for configuration and secrets.
- Exclusion of sensitive environment files, Terraform state and private keys from Git.

The existing EC2 security group is shared with the monitoring host and has broad inbound permissions. This is a known security limitation and should be reviewed before any production use.

Monitoring interfaces and the application are accessed through SSH tunnels.

## 11. Project Outcome

This capstone brings together application development, Docker, AWS, database integration, automated delivery and infrastructure monitoring in one practical project.

It demonstrates an end-to-end learning workflow while documenting the implementation, verification results and areas that still require improvement.
