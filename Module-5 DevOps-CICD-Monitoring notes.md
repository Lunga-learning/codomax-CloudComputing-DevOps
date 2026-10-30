# MODULE 5: DEVOPS, CI/CD & MONITORING

**Course:** Codomax Virtual Internship 2026 – Cloud Computing & DevOps
**Module:** 5
**Duration:** Day 21 – Day 25
**Priority:** High
**Project:** Automated Web Application Deployment Using GitHub Actions and AWS EC2
**Status:** CI/CD implementation and automated deployment completed

---

## 1. Introduction

Module 5 focuses on DevOps practices, Continuous Integration (CI), Continuous Delivery/Deployment (CD), and application monitoring.

The objective was to understand how developers can automate application testing and deployment instead of manually transferring application files to a server.

For this project, I created a simple HTML web application and implemented a CI/CD pipeline using GitHub Actions.

The pipeline automatically:

1. Detects changes pushed to the GitHub repository.
2. Checks out the application source code.
3. Validates the HTML.
4. Runs automated Python unit tests.
5. Connects securely to an AWS EC2 instance.
6. Transfers the updated application using SCP.
7. Verifies that the deployed application file exists.

The deployed application is served through Nginx on an AWS EC2 instance.

This project demonstrates a practical CI/CD workflow using Git, GitHub Actions, SSH, SCP, AWS EC2 and Nginx.

---

## 2. Learning Objectives

The main learning objectives were:

* Understand DevOps principles and practices.
* Understand Continuous Integration and Continuous Deployment.
* Learn how to automate application testing.
* Create and configure GitHub Actions workflows.
* Deploy applications automatically to AWS EC2.
* Configure SSH authentication for automated deployments.
* Understand environment variables and GitHub repository secrets.
* Verify application availability after deployment.
* Understand the importance of monitoring application health and deployment results.

---

## 3. Technologies and Tools Used

| Technology        | Purpose                          |
| ----------------- | -------------------------------- |
| AWS EC2           | Hosts the web application        |
| Amazon Linux 2023 | Operating system on EC2          |
| Git               | Version control                  |
| GitHub            | Source code repository           |
| GitHub Actions    | CI/CD automation                 |
| Python            | Automated application tests      |
| HTML              | Web application                  |
| Nginx             | Web server                       |
| SSH               | Secure remote server access      |
| SCP               | Secure application file transfer |
| MobaXterm         | SSH and SFTP client              |
| Linux             | Server administration            |

---

## 4. Understanding DevOps

DevOps combines development and operations practices to improve the speed, reliability and consistency of software delivery.

Traditionally, developers write application code and operations teams deploy and maintain applications.

DevOps encourages collaboration and automation throughout the software development lifecycle.

### Key DevOps principles

**Automation**

Automating repetitive activities such as testing, building and deployment.

**Collaboration**

Improving communication between development and operations teams.

**Continuous Integration**

Regularly integrating code changes into a shared repository and automatically testing them.

**Continuous Delivery and Deployment**

Preparing or automatically releasing validated application changes.

**Monitoring**

Observing application performance, availability and operational health.

---

## 5. Understanding CI/CD

CI/CD stands for Continuous Integration and Continuous Delivery or Continuous Deployment.

### 5.1 Continuous Integration (CI)

Continuous Integration involves regularly committing application changes to a shared repository.

Each change can trigger an automated pipeline that validates the application and runs tests.

In this project, CI performs:

* Repository checkout.
* Java environment setup for the HTML validator.
* Python environment setup.
* HTML validation.
* Automated Python unit tests.

### 5.2 Continuous Deployment (CD)

Continuous Deployment automatically transfers validated application changes to the target server.

In this project, CD:

* Connects to AWS EC2 using SSH.
* Transfers the application using SCP.
* Places the application in the Nginx web directory.
* Sets file permissions.
* Verifies that the application file exists and is not empty.

### Difference between CI and CD

| Continuous Integration | Continuous Deployment            |
| ---------------------- | -------------------------------- |
| Validates code changes | Releases validated changes       |
| Runs automated tests   | Transfers application files      |
| Detects errors early   | Updates the live application     |
| Runs before deployment | Runs after successful validation |

---

## 6. Project Architecture

The project uses GitHub Actions to automate the deployment of a web application to AWS EC2.

### Architecture flow

```text
Developer
    |
    v
Modify HTML Application
    |
    v
Git Commit
    |
    v
Git Push to GitHub
    |
    v
GitHub Repository
    |
    v
GitHub Actions Triggered
    |
    v
CI PIPELINE
    |
    +--> Checkout Repository
    |
    +--> Set Up Java
    |
    +--> Set Up Python
    |
    +--> Install HTML Validator
    |
    +--> Validate HTML
    |
    +--> Run Python Unit Tests
    |
    v
CI Successful
    |
    v
CD PIPELINE
    |
    +--> Connect to AWS EC2 using SSH
    |
    +--> Transfer index.html using SCP
    |
    +--> Set File Permissions
    |
    +--> Verify Deployment
    |
    v
AWS EC2
    |
    v
Nginx Web Server
    |
    v
Live Module 5 Website
```

### Deployment server information

| Resource              | Configuration       |
| --------------------- | ------------------- |
| Cloud provider        | AWS                 |
| Service               | EC2                 |
| Instance type         | t3.micro            |
| Operating system      | Amazon Linux 2023   |
| Region                | eu-north-1          |
| Web server            | Nginx               |
| Application directory | `/var/www/module5/` |
| Application file      | `index.html`        |
| Website path          | `/module5/`         |
| HTTP port             | 80                  |
| SSH port              | 22                  |

---

## 7. GitHub Repository Structure

The Module 5 project is stored in the main GitHub repository.

Relevant directory structure:

```text
codomax-CloudComputing-DevOps/
│
├── .github/
│   └── workflows/
│       └── module5-ci.yml
│
├── Module-3/
│
├── Module-4/
│
└── Module-5/
    └── DevOps-CICD-Monitoring/
        │
        ├── index.html
        │
        └── tests/
            └── test_app.py
```

### Important files

**index.html**

Contains the Module 5 web application.

**test_app.py**

Contains automated Python unit tests.

**module5-ci.yml**

Defines the GitHub Actions CI/CD pipeline.

---

## 8. Creating the Module 5 Web Application

The application was created using HTML.

Its purpose was to provide a simple website that could be deployed automatically through GitHub Actions.

The application includes:

* A Module 5 heading.
* Application status information.
* Deployment workflow information.
* A description of the Git workflow.
* An automatic deployment test message.

The application displays:

```text
Module 5: DevOps, CI/CD & Monitoring

Welcome to my DevOps learning project.

Application status: Running successfully!

Deployment workflow: GitHub Actions

Automatic deployment test: October 2026
```

The application is accessible through the EC2 public IP address.

---

## 9. Automated Testing with Python

Automated tests were created to verify that important application content exists.

Test file:

```text
Module-5/DevOps-CICD-Monitoring/tests/test_app.py
```

The tests check:

1. The HTML page title.
2. The main application heading.
3. The application status message.

### Running the tests locally

```bash
python3 -m unittest discover -s Module-5/DevOps-CICD-Monitoring/tests -v
```

### Expected result

```text
test_application_status ... ok
test_main_heading ... ok
test_page_title ... ok

Ran 3 tests

OK
```

### Why automated testing matters

Automated testing helps detect problems before an application is deployed.

Instead of manually checking the application after every change, tests can run automatically whenever qualifying code changes are pushed.

In this project, all three Python tests passed.

---

## 10. GitHub Actions CI/CD Pipeline

GitHub Actions was used to automate application validation, testing and deployment.

Workflow file:

```text
.github/workflows/module5-ci.yml
```

### Workflow triggers

The workflow is configured to run when:

* Changes are pushed to the `main` branch that affect the Module 5 project.
* Changes are made to the workflow file itself.
* A pull request targets the `main` branch and includes relevant changes.
* The workflow is manually started using `workflow_dispatch`.

### CI job

The CI job performs the following operations:

1. Checks out the repository using `actions/checkout`.
2. Sets up Java 17.
3. Sets up Python.
4. Installs `html5validator`.
5. Validates the application HTML.
6. Runs the Python unit tests.

HTML validation command:

```bash
html5validator --root Module-5/DevOps-CICD-Monitoring --also-check-css
```

Python test command:

```bash
python -m unittest discover -s Module-5/DevOps-CICD-Monitoring/tests -v
```

### CD job

The deployment job depends on the successful completion of the validation job.

It runs for pushes to the `main` branch.

The deployment process uses:

* `appleboy/scp-action` to transfer the application.
* `appleboy/ssh-action` to execute remote commands.

The application is copied to:

```text
/var/www/module5/
```

The remote deployment commands include:

```bash
chmod 644 /var/www/module5/index.html
test -s /var/www/module5/index.html
echo "Module 5 deployment completed successfully."
```

The commands ensure that the file has readable permissions and that the deployed file exists and is not empty.

---

## 11. Secure SSH Authentication

GitHub Actions needs secure access to the EC2 instance to deploy the application.

A dedicated Ed25519 SSH key pair was created for this purpose.

### SSH key configuration

The key pair was generated on the deployment EC2 instance.

The private key was stored in the GitHub repository secrets.

The corresponding public key was added to the EC2 user's authorized keys.

### GitHub repository secrets

The following secrets were configured:

| Secret name   | Purpose                                    |
| ------------- | ------------------------------------------ |
| `EC2_HOST`    | Public IP address of the deployment server |
| `EC2_SSH_KEY` | Private SSH key used by GitHub Actions     |

The private key is not stored in the GitHub repository source code.

### Why GitHub Secrets are important

Secrets allow workflows to use sensitive information without exposing it directly in workflow files.

Examples include:

* SSH private keys.
* API tokens.
* Passwords.
* Deployment credentials.

Sensitive values should never be committed to a public Git repository.

---

## 12. AWS EC2 Nginx Configuration

Nginx was used to serve the Module 5 application.

The existing Module 3 website was preserved.

Instead of replacing the original website, Module 5 was configured under a separate URL path.

### Application directory

```text
/var/www/module5/
```

### Nginx configuration

The following configuration was added to the existing server block:

```nginx
location = /module5 {
    return 301 /module5/;
}

location /module5/ {
    alias /var/www/module5/;
    index index.html;
    try_files $uri $uri/ =404;
}
```

This configuration:

* Redirects `/module5` to `/module5/`.
* Maps the `/module5/` URL to `/var/www/module5/`.
* Uses `index.html` as the default page.
* Returns a 404 response when the requested file cannot be found.

### Configuration validation

Before reloading Nginx, its configuration was tested:

```bash
sudo nginx -t
```

Nginx was then reloaded:

```bash
sudo systemctl reload nginx
```

The existing Module 3 website remained accessible.

---

## 13. Deployment Process

The deployment process was tested using an actual change to the HTML application.

### Step 1: Modify the application

A new paragraph was added:

```html
<p>Automatic deployment test: October 2026</p>
```

### Step 2: Review the change

The following command was used:

```bash
git diff -- Module-5/DevOps-CICD-Monitoring/index.html
```

This confirmed that only the intended line had changed.

### Step 3: Stage the change

```bash
git add Module-5/DevOps-CICD-Monitoring/index.html
```

### Step 4: Commit the change

```bash
git commit -m "Test automatic Module 5 deployment"
```

The resulting commit was:

```text
584672e
```

### Step 5: Push to GitHub

```bash
git push origin main
```

### Step 6: GitHub Actions execution

The push triggered the GitHub Actions workflow.

The CI job validated the HTML and ran the Python tests.

After successful validation, the deployment job connected to EC2 and transferred the updated application.

### Step 7: Verify deployment

The workflow executed the remote verification commands.

The deployment log confirmed:

```text
Module 5 deployment completed successfully.

Successfully executed commands to all hosts.
```

This demonstrated that the updated application was transferred successfully.

---

## 14. Testing and Verification

Several checks were performed to verify the application and deployment.

### 14.1 Automated tests

All three Python unit tests passed.

### 14.2 GitHub Actions

The workflow completed successfully.

The validation and deployment jobs both reported success.

### 14.3 Nginx HTTP response

The following command was executed on the deployment EC2 instance:

```bash
curl -I http://localhost/module5/
```

The response included:

```text
HTTP/1.1 200 OK
Server: nginx/1.30.5
Content-Type: text/html
```

This confirmed that Nginx was serving the Module 5 application successfully.

### 14.4 Live website

The public website was opened in a browser.

The new automatic deployment test message appeared on the live webpage.

This confirmed that a change pushed to GitHub was automatically deployed to AWS EC2.

---

## 15. Application Monitoring and Operational Checks

Monitoring is an important part of DevOps because deploying an application is not enough; its availability and operational health must also be checked.

During this project, basic operational verification was performed.

### Checks completed

| Check                        | Result      |
| ---------------------------- | ----------- |
| GitHub Actions execution     | Successful  |
| HTML validation              | Passed      |
| Python unit tests            | Passed      |
| SSH connection               | Successful  |
| SCP file transfer            | Successful  |
| Deployment file verification | Successful  |
| Nginx HTTP response          | HTTP 200 OK |
| Live website availability    | Confirmed   |

### Monitoring status

The project currently includes basic deployment and availability verification.

Dedicated Amazon CloudWatch dashboards, alarms and application performance monitoring have not yet been configured.

These are potential extensions for a more complete monitoring implementation.

---

## 16. Security Considerations

Security is important when automating deployments.

The following practices were applied:

1. A dedicated Ed25519 SSH key was created for automated deployment.
2. The private SSH key was stored in GitHub repository secrets.
3. The private key was not committed to Git.
4. SSH authentication used public-key authentication.
5. The deployment process used the `ec2-user` account.
6. The application file was assigned readable permissions using `chmod 644`.
7. Existing application content and the Module 3 website were preserved.

Secrets should be rotated if they are ever exposed or compromised.

---

## 17. Troubleshooting

### Problem 1: GitHub Actions deployment cannot connect to EC2

Possible causes:

* Incorrect EC2 public IP.
* Incorrect SSH private key.
* Public key missing from `authorized_keys`.
* SSH service unavailable.
* Security group not allowing the connection.

Useful checks:

```bash
sudo systemctl status sshd
```

```bash
sshd -T | grep -E 'pubkeyauthentication|passwordauthentication'
```

### Problem 2: Website returns HTTP 404

Possible causes:

* Application file missing.
* Incorrect Nginx alias.
* Incorrect application directory.
* Incorrect URL path.

Check the application file:

```bash
ls -l /var/www/module5/
```

### Problem 3: Nginx configuration error

Validate the configuration:

```bash
sudo nginx -t
```

Check the service:

```bash
sudo systemctl status nginx
```

### Problem 4: Automated tests fail

Run the tests locally:

```bash
python3 -m unittest discover -s Module-5/DevOps-CICD-Monitoring/tests -v
```

Review the failing test and correct the application or test code before pushing again.

---

## 18. Important Git Commands Learned

| Command                   | Purpose                   |
| ------------------------- | ------------------------- |
| `git status`              | Check working tree status |
| `git add <file>`          | Stage changes             |
| `git diff`                | Review changes            |
| `git commit -m "message"` | Create a commit           |
| `git push origin main`    | Push changes to GitHub    |
| `git log --oneline`       | View commit history       |
| `git pull origin main`    | Retrieve remote changes   |

These commands were used to manage the Module 5 project and trigger automated deployment.

---

## 19. Project Achievements

The following deliverables were completed:

* Created a Module 5 HTML application.
* Created automated Python unit tests.
* Configured HTML validation.
* Created a GitHub Actions CI workflow.
* Added an automated deployment job.
* Configured SSH authentication for GitHub Actions.
* Configured SCP application transfer.
* Configured Nginx to serve Module 5 separately.
* Successfully deployed the application to AWS EC2.
* Tested an actual code change through GitHub Actions.
* Confirmed that the updated webpage appeared online.

### Live application

**Module 5 website:**

http://13.50.235.157/module5/

### GitHub repository

https://github.com/Lunga-learning/codomax-CloudComputing-DevOps

---

## 20. Lessons Learned

This module provided practical experience with real DevOps deployment processes.

Key lessons include:

1. CI helps identify application errors before deployment.
2. Automated testing improves deployment confidence.
3. GitHub Actions can automate development and deployment tasks.
4. SSH provides secure remote server access.
5. SCP can transfer application files securely.
6. GitHub Secrets protect sensitive deployment credentials.
7. Nginx can serve multiple applications through separate URL paths.
8. Deployment must be verified after the workflow completes.
9. Successful deployment logs should be supported by actual application checks.
10. Monitoring is an ongoing operational responsibility, not just a deployment activity.

---

## 21. Conclusion

Module 5 demonstrated how to implement a practical CI/CD pipeline using GitHub Actions and AWS EC2.

The project successfully automated HTML validation, Python testing, SSH connectivity, application file transfer and deployment verification.

The application was deployed to an AWS EC2 instance and made publicly accessible through Nginx.

An additional code change was pushed to GitHub and automatically deployed. The updated webpage was then confirmed in the browser.

This module strengthened my understanding of DevOps principles, version control, automated testing, CI/CD workflows, SSH authentication and cloud application deployment.

The next improvement is to extend the project with dedicated monitoring using Amazon CloudWatch, including metrics, dashboards and alarms.

**Module 5 CI/CD implementation: Successfully completed.**
