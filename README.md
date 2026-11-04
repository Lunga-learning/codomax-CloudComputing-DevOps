# ☁️ Cloud Computing & DevOps Learning Portfolio

### Hands-on Learning | AWS | Linux | Networking | Terraform | Docker | CI/CD | Monitoring

Welcome to my Cloud Computing and DevOps learning portfolio!

This repository documents my practical learning journey as I develop skills in cloud infrastructure, Linux administration, networking, automation, containerisation, CI/CD and Infrastructure as Code (IaC).

My approach is to learn the concepts, practise them in a technical environment, document the process, troubleshoot problems, and record the results.

I am building on my background in IT operations and support while working towards opportunities in **Cloud Engineering, DevOps, and IT Infrastructure**.

---

## 🎯 Learning Objectives

My objectives are to:

- Develop a strong foundation in cloud computing and AWS.
- Strengthen Linux administration and troubleshooting skills.
- Understand IP addressing, DNS, routing, ports, and network security.
- Learn to define and organise infrastructure using Terraform.
- Build and containerise applications using Docker.
- Automate testing and deployment using CI/CD pipelines.
- Implement monitoring, metrics collection, and alerting.
- Build practical projects integrating cloud infrastructure and DevOps tools.
- Develop secure, repeatable, and cost-conscious cloud deployment habits.

---

## 🛠️ Technologies and Tools

| Technology | Learning Focus |
|---|---|
| Linux | Command-line administration, files, permissions, processes, and services |
| AWS | Cloud infrastructure and networking |
| Amazon EC2 | Virtual servers and Linux-based application deployment |
| Amazon Aurora PostgreSQL | Managed relational database services |
| Nginx | Web server installation and service management |
| Networking | IP addressing, DNS, ports, routing, and firewalls |
| Terraform | Infrastructure as Code, providers, variables, locals, and outputs |
| Terraform Modules | Reusable configurations and module organisation |
| Docker | Application containerisation and image building |
| Docker Compose | Multi-container application environments |
| Python | Application development and automated testing |
| Flask | Web application development |
| PostgreSQL | Relational database management |
| Git | Version control |
| GitHub | Source control, documentation, and portfolio development |
| GitHub Actions | Automated testing, image building, and deployment |
| Prometheus | Metrics collection and monitoring |
| Node Exporter | Linux host metrics |
| Grafana | Monitoring dashboards and visualisation |
| Alertmanager | Alert management and email notifications |
| AWS CLI | Command-line interaction with AWS services |

---

## 📚 Learning Progress: Days 6–30

My learning notes are organised by day to make progress easy to follow and review.

### 🐧 Days 6–21: Linux Administration and Networking

Topics covered include:

- Linux command-line navigation and file management.
- Filesystem usage and storage inspection.
- Users, groups, and file permissions.
- Process management and service administration.
- System logs and troubleshooting.
- IP addressing and DNS fundamentals.
- Network ports, firewalls, and AWS security groups.
- SSH access and secure file transfer.
- Linux server deployment workflows.
- Shell scripting fundamentals and backup practices.
- Deployment checklists and technical evidence organisation.

**Learning outcome:** Develop a structured approach to Linux administration, network troubleshooting, and server operations.

### ☁️ Days 22–23: AWS Networking

Topics covered include:

- Amazon Virtual Private Cloud (VPC).
- Subnets and IP address ranges.
- Route tables and routing concepts.
- Internet gateways.
- Security groups and traffic control.

**Learning outcome:** Understand how AWS networking components work together and why network configuration is important for secure cloud infrastructure.

### 🏗️ Days 24–30: Terraform and Infrastructure as Code

Topics covered include:

- Terraform configuration structure.
- AWS provider configuration.
- Variables and default values.
- Local values and derived configuration.
- Outputs for displaying configuration results.
- Variable files and command-line overrides.
- Root modules and reusable child modules.
- Terraform formatting, initialisation, validation, and planning.

**Learning outcome:** Build and validate structured Terraform configurations, understand how values flow between modules, and organise reusable infrastructure definitions.

**Important:** The Terraform exercises in Days 24–30 focused on configuration, validation, and planning. They did not deploy new AWS infrastructure.

---

## 🚀 Module 6 Capstone — DevOps Project Tracker

**Project:** Build, containerise, automate, deploy, and monitor a Flask-based DevOps Project Tracker application.

This capstone brings together several technologies and practices covered throughout my learning journey.

### Project Technologies

- Python and Flask for application development.
- PostgreSQL for relational database management.
- Docker and Docker Compose for containerisation.
- AWS EC2 for application hosting.
- Amazon Aurora PostgreSQL for managed database services.
- IAM authentication for database connectivity.
- Terraform for infrastructure configuration.
- Git and GitHub for version control.
- GitHub Actions for CI/CD automation.
- Prometheus and Node Exporter for metrics collection.
- Grafana for monitoring dashboards.
- Alertmanager and Brevo SMTP for email notifications.

### Application Features

- User authentication.
- Project management.
- Task management.
- Application dashboard.
- Health-check endpoint.
- PostgreSQL database integration.

### CI/CD Pipeline

The GitHub Actions workflow automates:

1. Application testing.
2. Code coverage reporting.
3. Docker image building.
4. Deployment to the existing AWS EC2 host.
5. Application health verification.

The deployment job runs after successful testing and is restricted to pushes to the `main` branch.

### Testing Results

The local automated test suite completed successfully:

- **13 tests passed.**
- **0 tests failed.**
- **75% overall code coverage.**

Local testing used Python 3.14.4. The GitHub Actions workflow uses Python 3.12.

### Monitoring and Alerting

The monitoring environment includes:

- Prometheus metrics collection.
- Node Exporter host monitoring.
- Grafana dashboards.
- CPU, memory, and filesystem warning rules.
- Alertmanager email notification integration through Brevo.

A manual Alertmanager email test was successfully delivered. Actual threshold-triggered Prometheus alert delivery remains subject to end-to-end validation.

### Project Documentation

The capstone includes dedicated documentation:

| Document | Description |
|---|---|
| [Project Overview](Module-6-Capstone/docs/README.md) | Project introduction, technologies, features, and testing |
| [Architecture](Module-6-Capstone/docs/architecture.md) | Application and infrastructure architecture |
| [Deployment Guide](Module-6-Capstone/docs/deployment.md) | Local Docker and AWS deployment |
| [CI/CD Pipeline](Module-6-Capstone/docs/ci-cd.md) | GitHub Actions testing and deployment workflow |
| [Monitoring Guide](Module-6-Capstone/docs/monitoring.md) | Prometheus, Grafana, Alertmanager, and notifications |

**Deployment note:** The application currently binds to localhost on the EC2 host and is accessed through an SSH tunnel. It is not documented as a publicly accessible application URL.

---

## 📂 Repository Structure

```text
codomax-CloudComputing-DevOps/
│
├── README.md
├── LEARNING_NOTES_DAYS_06-10.md
├── MODULE 4 DOCKER & CONTAINERIZATION.md
├── Module-5 DevOps-CICD-Monitoring notes.md
├── module-03-cloud-services-web-app-deployment.md
│
├── Module-4/
│   └── Docker-Containerization/
│       ├── Dockerfile
│       ├── compose.yaml
│       ├── compose-volume-test.yaml
│       ├── index.html
│       └── README.md
│
├── Module-5/
│   └── DevOps-CICD-Monitoring/
│
└── Module-6-Capstone/
    ├── app/
    ├── database/
    ├── monitoring/
    ├── tests/
    ├── terraform/
    ├── docs/
    │   ├── README.md
    │   ├── architecture.md
    │   ├── deployment.md
    │   ├── ci-cd.md
    │   └── monitoring.md
    ├── Dockerfile
    ├── docker-compose.yml
    ├── requirements.txt
    ├── requirements-dev.txt
    └── run.py
