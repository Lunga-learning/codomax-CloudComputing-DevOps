# ☁️ Cloud Computing & DevOps Learning Portfolio

### Hands-on Learning | AWS | Linux | Networking | Terraform | Docker | Kubernetes | CI/CD | Monitoring

Welcome to my Cloud Computing and DevOps learning portfolio!

This repository documents my practical learning journey as I develop skills in cloud computing, AWS infrastructure, Linux administration, networking, Infrastructure as Code (IaC), containerisation, Kubernetes, CI/CD automation, and monitoring.

My approach is to understand the concepts, practise them in a technical environment, document the process, troubleshoot problems, and record the results.

I am building on my background in IT operations and support while working towards opportunities in **Cloud Engineering, DevOps, and IT Infrastructure**.

---

## 🎯 Learning Objectives

My objectives are to:

- Develop a strong foundation in cloud computing and AWS.
- Strengthen Linux administration and troubleshooting skills.
- Understand IP addressing, DNS, routing, ports, and network security.
- Learn to manage and automate infrastructure using Terraform.
- Build and containerise applications using Docker.
- Understand Kubernetes fundamentals and container orchestration.
- Automate application testing and deployment using CI/CD pipelines.
- Implement monitoring, metrics collection, and alerting.
- Build practical projects integrating cloud infrastructure and DevOps tools.
- Develop secure, repeatable, and cost-conscious cloud deployment habits.

---

## 🛠️ Technologies and Tools

| Technology | Learning Focus |
|---|---|
| AWS | Cloud infrastructure and services |
| Amazon EC2 | Virtual servers and application hosting |
| Amazon S3 | Object storage |
| Amazon VPC | Cloud networking and network security |
| Amazon RDS / Aurora PostgreSQL | Managed relational databases |
| IAM | Identity and access management |
| AWS Systems Manager Parameter Store | Application configuration and secrets |
| Linux | Command-line administration, permissions, processes, and services |
| Networking | IP addressing, DNS, ports, routing, and firewalls |
| Terraform | Infrastructure as Code and reusable configurations |
| Nginx | Web server installation and management |
| Docker | Application containerisation and image building |
| Docker Compose | Multi-container application environments |
| Kubernetes | Container orchestration, Pods, and Deployments |
| Kind | Local Kubernetes learning environment |
| Python | Application development and automated testing |
| Flask | Web application development |
| PostgreSQL | Relational database management |
| Git | Version control |
| GitHub | Source control and portfolio development |
| GitHub Actions | CI/CD automation |
| Prometheus | Metrics collection and monitoring |
| Node Exporter | Linux host metrics |
| Grafana | Monitoring dashboards and visualisation |
| Alertmanager | Alert management and notifications |
| AWS CLI | Command-line interaction with AWS services |

---

# 📚 Learning Journey: Modules 1–6

## Module 01 — Cloud Computing Foundations
### Days 1–5

This module introduced the fundamental concepts of cloud computing and the core services used in cloud environments.

**Topics covered:**

- Introduction to cloud computing and its benefits.
- Infrastructure as a Service (IaaS), Platform as a Service (PaaS), and Software as a Service (SaaS).
- Public, private, and hybrid cloud deployment models.
- Data centres, AWS Regions, and Availability Zones.
- Virtualisation, hypervisors, and virtual machines.
- Introduction to Amazon EC2.
- AWS networking fundamentals, including VPCs and subnets.
- Public and private IP addresses, route tables, and internet gateways.
- AWS storage services, including S3, EBS, and EFS.
- Managed databases and the differences between SQL and NoSQL.
- Shared responsibility, IAM, and the principle of least privilege.
- Introduction to CloudWatch, monitoring, and logging.

**Practical learning:**

- Explored AWS services through the AWS Management Console.
- Launched and examined an EC2 instance.
- Inspected VPC and subnet configurations.
- Created an S3 bucket and uploaded a sample file.
- Explored AWS security and monitoring features.

**Learning outcome:** Developed an understanding of cloud computing concepts, AWS core services, infrastructure components, storage, security, and monitoring.

---

## Module 02 — Linux, Networking & Cloud Infrastructure
### Days 6–10

This module focused on Linux administration, network fundamentals, remote server management, and basic infrastructure operations.

**Topics covered:**

- Linux command-line navigation and file management.
- Filesystem structure and disk space inspection.
- Linux users, groups, and file permissions.
- Process and resource management.
- Service administration using systemd.
- System logs and troubleshooting.
- IP addressing and network interfaces.
- DNS resolution and connectivity testing.
- Network ports and listening services.
- SSH remote administration and secure file transfer.
- AWS VPC, subnet, route table, and security group concepts.
- AWS security group configuration and access restrictions.
- Shell scripting fundamentals.
- Backup and recovery fundamentals.

**Practical learning:**

- Worked with Linux users, groups, directories, and permissions.
- Inspected processes, services, system resources, and logs.
- Practised network troubleshooting and connectivity checks.
- Used SSH and SCP for remote server administration and file transfer.
- Examined AWS networking and security group configurations.

**Learning outcome:** Developed practical Linux administration and troubleshooting skills, together with a stronger understanding of networking and secure server operations.

**Learning notes:** [Module 2 — Linux, Networking & Cloud Infrastructure](LEARNING_NOTES_DAYS_06-10.md)

---

## Module 03 — Cloud Services & Web App Deployment
### Days 11–15

This module focused on using AWS cloud services to deploy and manage a web application.

**Topics covered:**

- AWS compute services using EC2.
- Object storage using Amazon S3.
- Managed database concepts using Amazon RDS.
- VPCs, subnets, route tables, and internet gateways.
- Security groups and network access control.
- IAM roles and permissions.
- Application configuration and environment variables.
- AWS Systems Manager Parameter Store.
- Secure storage of application secrets.
- Web server installation and management using Nginx.
- Infrastructure provisioning and configuration using Terraform.
- Application logging, monitoring, and resource awareness.

**Practical learning:**

- Provisioned an EC2 web server using Terraform.
- Installed and configured Nginx.
- Deployed a basic web page and verified that it was accessible.
- Used Terraform configuration files, variables, and outputs.
- Explored AWS Systems Manager Parameter Store.
- Created an RDS subnet group and a PostgreSQL security group with access restricted to the web server security group.

**Learning outcome:** Gained practical experience deploying a web server on AWS, using Terraform for infrastructure configuration, and exploring cloud networking, application configuration, and managed database services.

**Learning notes:** [Module 3 — Cloud Services & Web App Deployment](module-03-cloud-services-web-app-deployment.md)

---

## Module 04 — Docker & Containerization, Kubernetes Fundamentals
### Days 16–20

This module introduced containerisation and the fundamentals of running and managing containerised applications.

**Topics covered:**

- Containerisation concepts and benefits.
- Containers compared with virtual machines.
- Docker Engine, images, and containers.
- Writing Dockerfiles and building images.
- Running and managing Docker containers.
- Docker Hub and container images.
- Port mapping and container networking.
- Environment variables and configuration.
- Persistent storage using Docker volumes.
- Multi-container environments using Docker Compose.
- Kubernetes architecture and fundamentals.
- Kubernetes Pods and Deployments.
- Replica management and application self-healing.
- Introduction to local Kubernetes clusters using Kind.

**Practical learning:**

- Built a Docker image for an Nginx web application.
- Ran a container and tested access through port mapping.
- Created a Docker Compose environment.
- Tested persistent storage using a named volume.
- Inspected container logs and networking.
- Created a local Kubernetes cluster using Kind.
- Deployed an Nginx Pod and Kubernetes Deployment.
- Configured multiple replicas and observed Kubernetes replace a deleted managed Pod.

**Learning outcome:** Developed practical experience building and running Docker containers, managing multi-container applications, and understanding Kubernetes workloads, replicas, and self-healing.

**Learning notes:**
- [Module 4 — Docker & Containerization](<MODULE%204%20DOCKER%20%26%20CONTAINERIZATION.md>)
- [Kubernetes Fundamentals](<%23%20Kubernetes%20Fundamentals.md>)

**Practical project:** [Module 4 Docker Containerization](Module-4/Docker-Containerization/README.md)

---

## Module 05 — DevOps, CI/CD & Monitoring
### Days 21–25

This module focused on DevOps practices, version control, automated testing, and continuous integration and deployment.

**Topics covered:**

- DevOps principles and workflows.
- Version control using Git.
- Repository management using GitHub.
- Continuous Integration (CI).
- Continuous Deployment (CD).
- Automated application testing.
- HTML validation.
- GitHub Actions workflows.
- Deployment automation using SSH and SCP.
- Deploying web applications to an AWS EC2 host.
- Understanding the importance of application and infrastructure monitoring.

**Practical learning:**

- Created a simple web application.
- Developed Python unit tests.
- Validated application HTML.
- Created a GitHub Actions workflow.
- Automated testing through CI.
- Configured deployment to run after successful CI checks on pushes to the `main` branch.
- Used SSH and SCP to transfer application files to an EC2 host.
- Deployed the application using Nginx.
- Tested a code change through the GitHub Actions workflow and verified the updated website.

**Learning outcome:** Gained practical experience creating CI/CD workflows, automating application testing, and deploying application changes to an AWS-hosted web server.

**Learning notes:** [Module 5 — DevOps, CI/CD & Monitoring](<Module-5%20DevOps-CICD-Monitoring%20notes.md>)

---

## Module 06 — Cloud & DevOps Capstone Project
### Days 26–30

The final module brings together the technologies and practices explored throughout the learning journey in a practical DevOps capstone project.

### 🚀 Project: DevOps Project Tracker

**Project objective:** Build, containerise, test, deploy, and monitor a Flask-based DevOps Project Tracker application.

**Application features:**

- User authentication.
- Project management.
- Task management.
- Application dashboard.
- Health-check endpoint.
- PostgreSQL database integration.

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

### CI/CD Pipeline

The GitHub Actions workflow automates:

1. Application testing.
2. Code coverage reporting.
3. Docker image building.
4. Deployment to the existing AWS EC2 host.

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

### Deployment

The application currently runs on the EC2 host and binds to localhost. Access is provided through an SSH tunnel rather than a publicly accessible application URL.

### Capstone Documentation

| Document | Description |
|---|---|
| [Project Overview](Module-6-Capstone/docs/README.md) | Project introduction, technologies, features, and testing |
| [Architecture](Module-6-Capstone/docs/architecture.md) | Application and infrastructure architecture |
| [Deployment Guide](Module-6-Capstone/docs/deployment.md) | Local Docker and AWS deployment |
| [CI/CD Pipeline](Module-6-Capstone/docs/ci-cd.md) | GitHub Actions testing and deployment workflow |
| [Monitoring Guide](Module-6-Capstone/docs/monitoring.md) | Prometheus, Grafana, Alertmanager, and notifications |

**Learning outcome:** Applied cloud, Linux, networking, containerisation, application development, CI/CD, database integration, and monitoring concepts in one practical project.

---

## 📂 Repository Structure

```text
codomax-CloudComputing-DevOps/
│
├── README.md
│
├── LEARNING_NOTES_DAYS_06-10.md
├── module-03-cloud-services-web-app-deployment.md
├── MODULE 4 DOCKER & CONTAINERIZATION.md
├── # Kubernetes Fundamentals.md
├── Module-5 DevOps-CICD-Monitoring notes.md
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
```

---

## 🔐 Security & Good Practices

Throughout this learning journey, I aim to practise:

- Least-privilege access and appropriate IAM permissions.
- Restricting network access through security groups.
- Keeping credentials and secrets out of source control.
- Using environment variables and secure configuration.
- Documenting infrastructure and deployment processes.
- Considering AWS resource usage and cost.
- Testing changes before deployment.

---

## 📈 Learning Approach

Each module builds on the previous one:

**Learn → Practise → Build → Troubleshoot → Document → Improve**

The goal is not only to understand individual tools, but also to understand how they work together in real-world cloud and DevOps environments.

---

## 🎯 Career Direction

I am continuing to develop practical skills and build projects towards opportunities in:

- Cloud Engineering.
- DevOps Engineering.
- Linux and Infrastructure Administration.
- Cloud Infrastructure Support.
- CI/CD and Automation.

Thank you for visiting my learning portfolio!
