# MODULE 6: CLOUD & DEVOPS CAPSTONE
## DevOps Project Tracker — Days 26–30

**Programme:** Codomax Virtual Internship 2026  
**Track:** Cloud Computing & DevOps  
**Project:** DevOps Project Tracker  
**Level:** Capstone  
**Repository:** `codomax-CloudComputing-DevOps`

---

# 1. Module Overview

Module 6 brought together the knowledge and practical skills developed throughout the Cloud Computing and DevOps learning programme.

The objective was to develop a web application, connect it to a relational database, package it with Docker, automate testing and deployment, and introduce monitoring and alerting.

The capstone project was called **DevOps Project Tracker**.

It demonstrated how several technologies can work together to support an application lifecycle, from development through deployment and monitoring.

## Main objectives

1. Develop a web application using Python and Flask.
2. Integrate the application with PostgreSQL and Amazon Aurora PostgreSQL.
3. Implement authentication and project/task management.
4. Containerise the application using Docker.
5. Use Docker Compose to manage the application environment.
6. Deploy the application to an AWS EC2 environment.
7. Apply AWS IAM permissions and database authentication concepts.
8. Automate testing and deployment using GitHub Actions.
9. Introduce infrastructure configuration using Terraform.
10. Monitor application infrastructure using Prometheus, Node Exporter and Grafana.
11. Configure alert management and email notifications.
12. Document the architecture, deployment process and results.

## Project workflow

```text
Application Development
          |
          v
      Python / Flask
          |
          v
    PostgreSQL Database
          |
          v
  Docker / Docker Compose
          |
          v
       AWS EC2
          |
          v
     GitHub Actions
          |
          v
 Automated Testing and Build
          |
          v
       Deployment
          |
          v
 Prometheus / Node Exporter
          |
          v
        Grafana
          |
          v
 Alertmanager / Brevo SMTP
```

---

# 2. Technologies and Tools Used

This section records the technologies used in the capstone and their purposes.

## 2.1 Application development

| Technology | Recorded version | Purpose |
|---|---:|---|
| Python | 3.14.4 locally | Application development |
| Python | 3.12.15 in GitHub Actions | CI execution environment |
| Flask | 3.1.3 | Web application framework |
| Gunicorn | 23.0.0 | WSGI application server |
| SQLAlchemy | 2.1.6 | Database ORM |
| Flask-SQLAlchemy | 3.1.1 | Flask database integration |
| psycopg2-binary | 2.9.13 | PostgreSQL database driver |
| Flask-Login | 0.6.3 | User session management |
| Flask-Bcrypt | 1.0.1 | Password hashing integration |
| bcrypt | 5.0.0 | Password hashing |
| Flask-WTF | 1.3.0 | Form handling and CSRF protection |
| python-dotenv | 1.2.4 | Environment configuration |

## 2.2 Cloud and infrastructure

| Technology | Purpose |
|---|---|
| Amazon EC2 | Application hosting |
| Amazon Aurora PostgreSQL | Managed relational database service |
| PostgreSQL 17 | Relational database engine |
| AWS IAM | Identity and access management |
| IAM database authentication | Secure database access design |
| AWS CLI | AWS command-line interaction |
| Boto3 1.43.123 | AWS SDK for Python |
| Terraform | Infrastructure as Code |
| SSH | Secure remote server access |
| SCP | Secure file transfer |

## 2.3 Containers and automation

| Technology | Purpose |
|---|---|
| Docker | Application containerisation |
| Docker Engine | Building and running containers |
| Dockerfile | Instructions for building the application image |
| Docker Compose | Defining and managing application services |
| Git | Version control |
| GitHub | Source-code hosting and collaboration |
| GitHub Actions | Automated testing, image building and deployment |

## 2.4 Testing and monitoring

| Technology | Purpose |
|---|---|
| pytest 9.2.0 | Automated application testing |
| pytest-cov 7.1.0 | Test coverage reporting |
| coverage 7.17.0 | Code coverage measurement |
| Prometheus | Metrics collection and monitoring |
| Node Exporter | Linux host metrics |
| Grafana | Monitoring dashboards |
| Alertmanager | Alert management and notification routing |
| Brevo SMTP | Email notification delivery |
| curl | HTTP endpoint verification |
| Mermaid | Architecture diagrams and documentation |

**Version note:** Versions are included where they were recorded in the project dependency or execution information. Versions for Docker, Terraform, Prometheus, Grafana, Node Exporter and Alertmanager should be checked against their actual installation records before publishing a version-specific inventory.

---

# 3. Day 26 — Application Development and Database Integration

## Objective

The first stage of the capstone focused on developing the DevOps Project Tracker application and understanding how a web application communicates with a relational database.

## 3.1 Python

Python was used as the main programming language.

It provided the application logic and connected the different application components.

The project used Python locally and a separate Python version in the automated GitHub Actions environment.

Recorded environments:

- Local development: Python 3.14.4.
- GitHub Actions: Python 3.12.15.

This distinction is important because the local development environment and the CI environment do not necessarily use the same Python version.

## 3.2 Flask

Flask was used as the web framework.

It provides the functionality required to create web routes, process requests, manage application logic and return responses.

The application included the following features:

- User authentication.
- Project management.
- Task management.
- Application dashboard.
- Database integration.
- Health-check endpoint.

### Flask application structure

The project separated application responsibilities into different modules.

The recorded application modules included:

```text
app/
├── __init__.py
├── auth.py
├── models.py
├── projects.py
└── tasks.py
```

The purpose of this structure was to keep application functionality organised.

| File | Responsibility |
|---|---|
| `__init__.py` | Application creation and configuration |
| `auth.py` | Authentication functionality |
| `models.py` | Database models |
| `projects.py` | Project management functionality |
| `tasks.py` | Task management functionality |

## 3.3 Database integration

PostgreSQL was used as the relational database technology.

The application used SQLAlchemy and Flask-SQLAlchemy to interact with the database.

### Understanding SQLAlchemy

SQLAlchemy is an Object Relational Mapper (ORM).

An ORM allows application developers to interact with database records through Python objects instead of writing every database operation as raw SQL.

For example, a project can be represented as a Python model, while SQLAlchemy manages the database operations associated with that model.

### PostgreSQL driver

The application used:

`psycopg2-binary 2.9.13`

This driver enables Python applications to communicate with PostgreSQL databases.

### Amazon Aurora PostgreSQL

Amazon Aurora PostgreSQL was included as the managed database target in the capstone architecture.

Aurora is an AWS managed relational database service compatible with PostgreSQL.

It is important to distinguish the database technologies:

- PostgreSQL 17 refers to the recorded PostgreSQL engine version.
- Amazon Aurora PostgreSQL refers to the managed AWS database service.

The application architecture included database connectivity and IAM database authentication considerations.

## 3.4 User authentication

Authentication was another important application feature.

The project used:

- Flask-Login 0.6.3.
- Flask-Bcrypt 1.0.1.
- bcrypt 5.0.0.

Flask-Login supports user session management.

Bcrypt provides password hashing functionality.

Password hashing is important because applications should not store users' passwords as plain text.

## 3.5 Environment configuration

The application used environment-based configuration.

The `python-dotenv` package was included to support loading environment variables from a local configuration file.

The purpose of environment variables is to separate application configuration from application source code.

Sensitive configuration should not be committed to GitHub.

Examples of sensitive values include:

- Database passwords.
- SMTP credentials.
- AWS credentials.
- Secret keys.
- API tokens.

## 3.6 Application server

Gunicorn was included as the production WSGI server.

Recorded version:

`gunicorn 23.0.0`

A development server is useful when developing an application, but Gunicorn provides a dedicated application-serving process for deployment.

## Learning outcome

Day 26 connected application development with database management.

I learned how Python and Flask work together to provide application functionality, how SQLAlchemy communicates with PostgreSQL, and why authentication and secure configuration are important.

---

# 4. Day 27 — Docker and Application Containerisation

## Objective

The next stage focused on packaging the application and its dependencies into a Docker image.

Containerisation helps applications run consistently across supported environments.

## 4.1 What is Docker?

Docker is a platform used to build and run containers.

A container packages an application with the dependencies it requires.

This helps reduce differences between development and deployment environments.

### Important Docker concepts

| Concept | Explanation |
|---|---|
| Docker Engine | Software responsible for building and running containers |
| Docker image | Packaged application template |
| Docker container | Running instance of an image |
| Dockerfile | Instructions used to build an image |
| Docker Compose | Tool for managing multiple application services |
| Docker volume | Persistent storage managed by Docker |
| Port mapping | Connects a host port to a container port |
| Docker Hub | Registry for storing and distributing images |

## 4.2 Dockerfile

The capstone included a Dockerfile.

The Dockerfile defined how the application image should be built.

The recorded CI build output confirmed that the Dockerfile was loaded and used to build the application image.

The build included these stages:

1. Load the Dockerfile.
2. Load the Python base image.
3. Set the working directory.
4. Copy the requirements file.
5. Install Python dependencies.
6. Copy the application files.
7. Export the completed image.

The build used the Python 3.12 slim base image.

## 4.3 Docker image building

The GitHub Actions build log recorded this command:

```bash
docker build -t devops-project-tracker:ci .
```

Explanation:

- `docker build` starts an image build.
- `-t` assigns a name and tag to the image.
- `devops-project-tracker` is the image name.
- `ci` is the image tag.
- `.` identifies the current directory as the build context.

The CI build successfully created the image:

`devops-project-tracker:ci`

This confirmed that the application could be packaged into a Docker image during the automated workflow.

## 4.4 Docker Compose

Docker Compose was included to manage the application environment.

Instead of manually starting each required service separately, Compose allows services and their configuration to be defined in a YAML file.

The capstone repository included:

```text
docker-compose.yml
```

Docker Compose is useful for coordinating an application and its supporting services.

It can define:

- Application containers.
- Database services.
- Environment variables.
- Networks.
- Volumes.
- Service dependencies.

## 4.5 Containerisation benefits

The practical benefits of Docker include:

**Portability:** The application can be packaged and moved between supported environments.

**Consistency:** The same image can be used across different stages of the deployment process.

**Isolation:** Containers run in separate environments.

**Repeatability:** Application deployment can follow a consistent configuration.

**Efficiency:** Containers generally use fewer resources than full virtual machines.

## Learning outcome

Day 27 demonstrated how Docker packages an application and its dependencies.

I learned the difference between a Docker image and a container, how Dockerfiles define image builds, and how Docker Compose helps organise application services.

The successful CI image build provided evidence that the application could be packaged automatically.

---

# 5. Day 28 — AWS Deployment, Infrastructure and CI/CD

## Objective

This stage focused on deploying the application in an AWS environment and automating important development and deployment tasks.

## 5.1 Amazon EC2

Amazon EC2 provided the cloud compute environment used for application hosting.

An EC2 instance is a virtual server running on AWS infrastructure.

The project used an existing EC2 host rather than treating the application as a publicly exposed service.

The application was configured to bind to localhost and was accessed through an SSH tunnel.

This means the application was not documented as a publicly accessible website.

## 5.2 SSH and SCP

SSH was used for secure remote administration.

SCP supports secure file transfers between local and remote systems.

These tools are important when managing a Linux server remotely.

### SSH purpose

SSH provides an encrypted connection to a remote server.

It can be used to:

- Execute commands remotely.
- Inspect application services.
- Troubleshoot deployment problems.
- Manage server configuration.

### SCP purpose

SCP transfers files securely over SSH.

It can be used to transfer application files, configuration files and deployment-related files.

Private keys and credentials must be protected and must never be committed to the repository.

## 5.3 AWS IAM

AWS IAM controls access to AWS resources.

The capstone included IAM-based access considerations for the application and its database.

IAM policies determine which AWS actions an identity is permitted to perform.

The principle of least privilege is important.

An application should receive only the permissions it requires.

## 5.4 IAM database authentication

The project included an IAM database authentication design for PostgreSQL-compatible database access.

IAM database authentication allows authorised identities to authenticate to supported database configurations using temporary authentication tokens rather than relying exclusively on long-lived database passwords.

This is an important security concept because it connects AWS identity management with database access control.

## 5.5 Boto3

Boto3 is the AWS SDK for Python.

Recorded version:

`boto3 1.43.123`

It allows Python applications and scripts to interact with AWS services programmatically.

For example, Boto3 can be used to interact with AWS APIs without manually performing every operation through the AWS Console.

## 5.6 Terraform

Terraform was included as the Infrastructure as Code tool.

Infrastructure as Code allows infrastructure configuration to be represented in files.

Instead of relying entirely on manual configuration through the AWS Console, Terraform allows infrastructure definitions to be managed as code.

Important Terraform commands include:

```bash
terraform init
terraform fmt
terraform validate
terraform plan
terraform apply
```

Purpose:

| Command | Purpose |
|---|---|
| `terraform init` | Initialises the working directory |
| `terraform fmt` | Formats Terraform configuration |
| `terraform validate` | Checks configuration validity |
| `terraform plan` | Previews proposed infrastructure changes |
| `terraform apply` | Applies the proposed changes |

These are command references for the Terraform workflow. They should not be interpreted as proof that every command was executed during this particular capstone.

## 5.7 Git and GitHub

Git was used for version control.

GitHub hosted the project repository and provided the platform for automated workflows.

Version control is important because it allows developers to track changes, review project history and maintain a record of application development.

## 5.8 GitHub Actions

GitHub Actions was used to automate the CI/CD workflow.

The project workflow automated:

1. Application testing.
2. Code coverage reporting.
3. Docker image building.
4. Deployment to the existing AWS EC2 host.
5. Application health verification.

The deployment job was configured to run after successful testing and was restricted to pushes to the `main` branch.

### Recorded CI workflow environment

The GitHub Actions log showed:

```text
Python 3.12.15
pytest 9.2.0
pytest-cov 7.1.0
```

### Recorded testing command

```bash
python -m pytest --cov=app --cov-report=term-missing
```

Explanation:

- `python -m pytest` runs the pytest test framework.
- `--cov=app` measures coverage of the application package.
- `--cov-report=term-missing` displays coverage and identifies lines that were not covered by tests.

The workflow collected 13 tests.

All 13 passed.

### Recorded Docker build command

```bash
docker build -t devops-project-tracker:ci .
```

The Docker build completed successfully.

## 5.9 CI/CD workflow

The overall workflow can be represented as:

```text
Developer changes code
          |
          v
     Git commit
          |
          v
    Push to GitHub
          |
          v
   GitHub Actions starts
          |
          v
 Install dependencies
          |
          v
    Run pytest
          |
          v
 Generate coverage report
          |
          v
    Build Docker image
          |
          v
   Deployment job
          |
          v
      AWS EC2
          |
          v
 Application health check
```

## Learning outcome

Day 28 connected application development with cloud deployment and automation.

I learned how EC2 provides the hosting environment, how IAM controls access, how Terraform represents infrastructure as code, and how GitHub Actions can automate testing and deployment.

The CI workflow provided evidence that the application tests passed and the Docker image built successfully.

---

# 6. Day 29 — Monitoring, Metrics and Alerting

## Objective

The next stage focused on monitoring the application environment and understanding how infrastructure metrics can be collected, visualised and used to generate alerts.

Monitoring is important because a deployed application needs to be observed after deployment.

It helps identify resource pressure, service problems and potential failures.

## 6.1 Prometheus

Prometheus was used as the metrics collection and monitoring technology.

Prometheus collects and stores metrics from configured targets.

These metrics can help operators understand the condition and performance of an environment.

Examples of monitoring measurements include:

- CPU utilisation.
- Memory utilisation.
- Filesystem usage.
- Service availability.
- Application-related metrics where exposed.

## 6.2 Node Exporter

Node Exporter provides host-level metrics for Prometheus.

It is commonly used to expose Linux system information.

Prometheus can scrape the metrics exposed by Node Exporter.

The relationship is:

```text
Linux EC2 Host
      |
      v
  Node Exporter
      |
      v
   Prometheus
      |
      v
    Grafana
```

Node Exporter and Prometheus serve different purposes:

- Node Exporter exposes system metrics.
- Prometheus collects and stores those metrics.

## 6.3 Grafana

Grafana was included for monitoring dashboards and visualisation.

It allows collected metrics to be presented in dashboards.

Dashboards can help operators identify trends and monitor system health.

For example, a dashboard can display CPU usage over time or show available filesystem capacity.

## 6.4 Alertmanager

Alertmanager was included for alert management.

It receives alerts generated by the monitoring system and manages how those alerts are grouped, routed and delivered.

For example, a monitoring rule may identify a condition that requires attention.

Alertmanager can then route the alert to a configured notification destination.

## 6.5 Brevo SMTP

Brevo SMTP was used as the email notification service.

SMTP is the protocol used for sending email between systems.

The project included an email notification configuration using Brevo.

A manual Alertmanager email test was successfully delivered.

This confirmed that the manual email notification test worked.

However, a successful manual email test does not automatically prove that every monitoring rule can trigger an alert and deliver it end to end.

## 6.6 Monitoring architecture

The monitoring components can be represented as:

```text
       Linux EC2 Host
              |
              v
         Node Exporter
              |
              v
          Prometheus
              |
       Metrics and Rules
              |
              v
        Alertmanager
              |
              v
          Brevo SMTP
              |
              v
        Email Notification


          Prometheus
              |
              v
           Grafana
              |
              v
       Monitoring Dashboard
```

## 6.7 Monitoring and alerting concepts

| Component | Responsibility |
|---|---|
| Node Exporter | Exposes Linux host metrics |
| Prometheus | Collects and stores metrics |
| Prometheus rules | Evaluate configured monitoring conditions |
| Grafana | Displays monitoring dashboards |
| Alertmanager | Manages and routes alerts |
| Brevo SMTP | Delivers email notifications |

## Learning outcome

Day 29 introduced the importance of monitoring after deployment.

I learned that deploying an application is only one part of operating a system.

The system must also be observed so that problems can be identified and investigated.

Prometheus, Node Exporter and Grafana support metrics collection and visualisation, while Alertmanager and Brevo SMTP support notification delivery.

---

# 7. Day 30 — Testing, Validation and Capstone Review

## Objective

The final stage focused on reviewing the application, checking automated test results, validating the Docker image build and reviewing the overall project architecture.

Testing is important because it provides evidence that application functionality works as expected.

## 7.1 Automated testing with pytest

The project used pytest for automated application testing.

Recorded version:

`pytest 9.2.0`

The test suite contained:

```text
tests/
└── test_app.py
```

The recorded GitHub Actions test command was:

```bash
python -m pytest --cov=app --cov-report=term-missing
```

## 7.2 Test results

The actual GitHub Actions execution reported:

```text
platform linux
Python 3.12.15
pytest-9.2.0
pluggy-1.7.0

collected 13 items

tests/test_app.py ............. [100%]

13 passed in 2.68s
```

### Test summary

| Result | Value |
|---|---:|
| Tests collected | 13 |
| Tests passed | 13 |
| Tests failed | 0 |
| Total code coverage | 82% |
| Statements | 287 |
| Missed statements | 51 |

The recorded coverage by application module was:

| Application module | Coverage |
|---|---:|
| `app/__init__.py` | 74% |
| `app/auth.py` | 78% |
| `app/models.py` | 92% |
| `app/projects.py` | 89% |
| `app/tasks.py` | 82% |
| **Total** | **82%** |

### Understanding code coverage

Code coverage measures how much of the application code is executed during testing.

The project achieved 82% coverage.

This means that 82% of the measured application statements were covered by the recorded test run.

It does not mean that the application is completely free from bugs.

The remaining uncovered code represents an opportunity to improve the test suite.

## 7.3 Docker build validation

The GitHub Actions workflow also built the Docker image.

Recorded command:

```bash
docker build -t devops-project-tracker:ci .
```

The build output confirmed:

- Docker loaded the Dockerfile.
- The Python 3.12 slim base image was retrieved.
- The requirements file was copied.
- Python dependencies were installed.
- Application files were copied.
- The image was exported successfully.
- The image was tagged `devops-project-tracker:ci`.

This provided evidence that the application image could be built in the CI environment.

## 7.4 Application health verification

The project included a health-check endpoint.

A health endpoint provides a way to check whether an application is responding.

The project deployment workflow included an application health-verification stage.

The general HTTP verification command is:

```bash
curl -I http://localhost:PORT/health
```

Here, `PORT` represents the configured application port.

The command is a reusable verification pattern. The exact port and route should be checked against the deployment configuration before using it.

A successful HTTP response indicates that the endpoint responded to the request.

## 7.5 Deployment access and security

The application was configured to bind to localhost on the EC2 host.

It was accessed using an SSH tunnel.

This means that the application was not being presented as a publicly accessible application URL.

This approach reduces direct public exposure of the application service.

It also demonstrates the use of SSH for controlled remote access.

## 7.6 Documentation

The capstone included dedicated documentation:

| Document | Purpose |
|---|---|
| `docs/README.md` | Project overview and introduction |
| `docs/architecture.md` | Application and infrastructure architecture |
| `docs/deployment.md` | Local Docker and AWS deployment |
| `docs/ci-cd.md` | GitHub Actions workflow |
| `docs/monitoring.md` | Prometheus, Grafana, Alertmanager and notifications |

Mermaid was included for architecture diagrams.

Architecture documentation helps explain how application components, databases, infrastructure and monitoring services work together.

## Learning outcome

Day 30 brought together the work completed during the capstone.

The automated test suite passed all 13 tests, achieving 82% code coverage.

The Docker image build completed successfully.

The project demonstrated how application development, database integration, containerisation, cloud hosting, CI/CD automation and monitoring can form part of a complete DevOps workflow.

---

# 8. Complete Project Technology Inventory

The following is the consolidated inventory of the tools and technologies recorded during the capstone.

| Category | Tools |
|---|---|
| Programming | Python |
| Web framework | Flask |
| Application server | Gunicorn |
| Database | PostgreSQL 17, Amazon Aurora PostgreSQL |
| ORM | SQLAlchemy, Flask-SQLAlchemy |
| Database driver | psycopg2-binary |
| Authentication | Flask-Login, Flask-Bcrypt, bcrypt |
| Forms and security | Flask-WTF |
| Configuration | python-dotenv, environment variables |
| AWS SDK | Boto3 |
| Cloud infrastructure | Amazon EC2, Amazon Aurora |
| Cloud security | AWS IAM, IAM database authentication |
| Infrastructure as Code | Terraform |
| Containerisation | Docker, Docker Engine |
| Container orchestration | Docker Compose |
| Version control | Git |
| Source hosting | GitHub |
| CI/CD | GitHub Actions |
| Testing | pytest |
| Coverage | pytest-cov, coverage |
| Monitoring | Prometheus |
| Host metrics | Node Exporter |
| Dashboards | Grafana |
| Alert management | Alertmanager |
| Email delivery | Brevo SMTP |
| Remote administration | SSH |
| File transfer | SCP |
| HTTP testing | curl |
| Documentation | Markdown, Mermaid |

---

# 9. Security Practices

Security was an important consideration throughout the capstone.

The project involved several security-related technologies and practices.

## 9.1 Password security

Passwords should never be stored as plain text.

The application included bcrypt-based password hashing.

## 9.2 Environment variables

Sensitive configuration should be separated from application source code.

Examples include:

- Database credentials.
- SMTP passwords.
- Application secret keys.
- API credentials.

## 9.3 AWS IAM

IAM should follow the principle of least privilege.

Application identities should receive only the permissions needed to perform their responsibilities.

## 9.4 Database security

Database access should be restricted to authorised application components.

The database should not be unnecessarily exposed to the public internet.

IAM database authentication provides an additional approach to controlling access to supported PostgreSQL-compatible database configurations.

## 9.5 SSH security

SSH provides encrypted remote access.

Private keys must be protected and excluded from version control.

## 9.6 GitHub security

The following should never be committed to a public repository:

- `.env` files containing secrets.
- AWS credentials.
- Database passwords.
- Private SSH keys.
- Terraform state files containing sensitive values.
- SMTP credentials.

Sensitive values should be managed through appropriate secrets-management facilities.

---

# 10. Troubleshooting and Important Lessons

The capstone reinforced several important operational lessons.

## Application development

A web application should be separated into manageable modules.

This makes it easier to maintain authentication, database models, project management and task management functionality.

## Database integration

Database connectivity depends on several components working together:

- Application configuration.
- Database availability.
- Network connectivity.
- Database authentication.
- Database permissions.

A database connection failure does not necessarily mean that the application code itself is incorrect.

## Docker

A successful Docker image build confirms that the image can be created.

It does not, by itself, prove that every container will start correctly or that every application feature works.

Container runtime checks and application health checks are also important.

## CI/CD

Automated testing helps identify application problems before deployment.

A deployment should depend on successful validation rather than being triggered regardless of test results.

## Monitoring

Metrics collection and alerting are separate but connected responsibilities.

A dashboard displaying metrics does not automatically mean that alerts are configured correctly.

Alert delivery must be tested separately.

## Security

The project reinforced the importance of protecting credentials, restricting access and avoiding unnecessary public exposure.

---

# 11. Verified Results and Outstanding Validation

It is important to distinguish between completed work and work that still needs additional verification.

## Verified results

| Item | Recorded result |
|---|---|
| Flask application | Developed with authentication and project/task functionality |
| Database integration | PostgreSQL integration included |
| Docker image | CI image build completed successfully |
| Automated tests | 13 tests passed |
| Test failures | 0 |
| Code coverage | 82% |
| GitHub Actions | Automated testing and image building succeeded |
| Manual email test | Alertmanager email test successfully delivered |
| Application access | Configured for localhost access through SSH tunnelling |
| Project documentation | Dedicated architecture, deployment, CI/CD and monitoring documents included |

## Items requiring further verification

| Item | What still needs to be checked |
|---|---|
| Prometheus alerting | Confirm a real threshold condition triggers an alert |
| Alertmanager integration | Confirm the triggered alert reaches Alertmanager |
| End-to-end email delivery | Confirm the threshold-triggered alert results in an email |
| Deployment verification | Review the actual deployment job output and health-check result |
| Terraform | Confirm which infrastructure resources were actually applied |
| Database authentication | Verify a successful live IAM database authentication connection |
| Monitoring dashboards | Confirm the final dashboards and targets are operational |

A manual email test is useful evidence, but it should not be confused with a fully verified threshold-triggered alert.

Likewise, a successful Docker build does not automatically prove that every deployment and runtime integration is working.

---

# 12. Final Architecture

The overall capstone architecture can be summarised as follows:

```text
                  DEVELOPER
                      |
                      v
                Git / GitHub
                      |
                      v
               GitHub Actions
                      |
              +-------+-------+
              |               |
              v               v
          pytest          Docker Build
              |               |
              +-------+-------+
                      |
                      v
                 AWS EC2
                      |
                      v
              Flask Application
                      |
                      v
              PostgreSQL / Aurora
                      |
                      v
                Health Endpoint


              MONITORING LAYER

                  EC2 Host
                      |
                      v
                 Node Exporter
                      |
                      v
                  Prometheus
                      |
              +-------+-------+
              |               |
              v               v
            Grafana       Alertmanager
                              |
                              v
                           Brevo SMTP
                              |
                              v
                       Email Notification
```

---

# 13. Overall Module Reflection

Module 6 was an important stage in my Cloud Computing and DevOps learning journey because it brought together several technologies into one practical capstone project.

I developed a DevOps Project Tracker application using Python and Flask and integrated it with a relational database.

I used Docker to package the application and GitHub Actions to automate testing and image building.

I also worked with AWS infrastructure concepts, EC2 hosting, IAM permissions, database authentication and Terraform.

The monitoring component introduced Prometheus, Node Exporter, Grafana and Alertmanager. Brevo SMTP was used for email notification testing.

The automated testing results provided measurable evidence of the application's progress:

- 13 tests passed.
- 0 tests failed.
- 82% code coverage.
- Successful Docker image build.

The most important lesson was understanding that DevOps is not simply about deploying an application.

It involves connecting development, testing, packaging, infrastructure, deployment, security, monitoring and continuous improvement.

This capstone helped me understand how these different responsibilities fit together in a practical application environment.

## Final outcome

I completed a practical DevOps capstone that brought together application development, relational database integration, containerisation, cloud infrastructure, CI/CD automation, testing and monitoring.

The project provided practical experience with technologies commonly used in modern cloud and DevOps environments.