MODULE 4: DOCKER & CONTAINERIZATION

Codomax Virtual Internship 2026 — Cloud Computing & DevOps

1. Introduction to Containerization
What is containerization?

Containerization is a technology that packages an application and its required dependencies into a container so that it can run consistently across different environments.

For example, we created a web application and ran it inside a Docker container on our AWS EC2 instance.

What is Docker?

Docker is a platform used to build, package, and run applications inside containers.

Docker helps developers deploy applications consistently without needing to install all application dependencies directly on the host operating system.

Benefits of Docker
Portability: Applications can run across different supported environments.
Consistency: Containers help reduce differences between development and deployment environments.
Isolation: Applications run in separate containers with isolated processes and resources.
Efficiency: Containers generally require fewer resources than full virtual machines.
Scalability: Containers can be replicated to handle increased workloads.
Faster deployment: Applications can be packaged and started quickly.
Containers versus virtual machines
Feature	Containers	Virtual machines
Operating system	Share the host kernel	Each VM runs its own guest OS
Resource usage	Generally lower	Generally higher
Startup time	Usually seconds or less	Often longer
Isolation	Process-level and configurable	Typically stronger hardware-level isolation
Portability	High	High, depending on the hypervisor and platform
Example	Docker container	EC2 instance running a guest OS

Remember: A container is not the same as a virtual machine. Containers share the host kernel, whereas virtual machines run separate guest operating systems.

2. Important Docker Concepts

Understanding these terms is essential.

Concept	Meaning
Docker Engine	The software responsible for building and running containers
Docker image	A packaged template used to create containers
Docker container	A running or stopped instance of an image
Dockerfile	A text file containing instructions to build an image
Docker Hub	An online registry where Docker images can be stored and shared
Docker Compose	A tool for defining and managing applications using YAML configuration
Docker volume	Storage managed by Docker that can persist beyond a container's lifetime
Port mapping	Connects a host port to a port inside a container
Container registry	A service that stores and distributes container images
Understanding the relationship

The typical workflow is:

Dockerfile → Docker Image → Docker Container → Running Application

In our project:

We created a Dockerfile.
We built an image named my-docker-webapp:1.0.
We used that image to run our web application.
We configured Docker Compose to manage the container.
3. Understanding the Dockerfile

A Dockerfile defines the instructions Docker uses to build an image.

Our project used this Dockerfile:

FROM nginx:alpine

COPY index.html /usr/share/nginx/html/index.html

EXPOSE 80
Explanation of each instruction

FROM nginx:alpine

Uses the lightweight Alpine-based Nginx image as the starting point.

Nginx is a web server that serves our HTML page.

COPY index.html /usr/share/nginx/html/index.html

Copies our HTML file into the directory from which Nginx serves web content.

EXPOSE 80

Documents that the containerized application listens on port 80.

Important: EXPOSE does not publish the port to the host automatically. Port publishing is configured separately.

What is index.html?

index.html is the webpage displayed by our application.

Our page contains:

The title Docker Containerization Project
The heading My First Docker Web Application
A message confirming that the application was deployed inside a Docker container.
The module name.
4. Building and Running Docker Containers

These are important commands from our practical work.

Check the Docker version
sudo docker --version

Displays the installed Docker version.

Check whether Docker is running
sudo systemctl status docker

Displays the status of the Docker service.

Build a Docker image
cd /home/ec2-user/docker-containerization-lab

Then:

sudo docker build -t my-docker-webapp:1.0 .

Explanation:

docker build builds an image.
-t assigns a name and tag.
my-docker-webapp is the image name.
1.0 is the image tag.
. specifies the current directory as the build context.
List Docker images
sudo docker images

Displays images stored locally.

Run a container
sudo docker run -d \
  --name my-docker-webapp-container \
  -p 8080:80 \
  my-docker-webapp:1.0

Explanation:

-d: Runs the container in the background.
--name: Assigns a container name.
-p 8080:80: Maps host port 8080 to container port 80.
my-docker-webapp:1.0: Specifies the image.

Important: This command was our standalone-container approach. Our Docker Compose project also uses port 8080, so do not run both versions simultaneously unless you have checked that port 8080 is available.

List running containers
sudo docker ps

Shows running containers.

To include stopped containers:

sudo docker ps -a
View container logs
sudo docker logs my-docker-webapp-container

Shows logs for the standalone container.

For our Compose-managed application:

sudo docker compose logs web
Stop a container
sudo docker stop my-docker-webapp-container

Stops the standalone container.

Remove a stopped container
sudo docker rm my-docker-webapp-container

Removes the standalone container. It must be stopped first.

Test the application
curl http://localhost:8080

This sends an HTTP request to the application through port 8080.

In our project, it returned the HTML page successfully.

5. Docker Port Mapping and Networking

Port mapping allows traffic arriving at a host port to reach a service listening inside a container.

Our project uses:

Host port 8080 → Container port 80

For example:

-p 8080:80

The first port is the host port; the second is the container port.

Why did we use port 8080?

Our EC2 instance already had another web application using host port 80.

We used port 8080 for the Docker application to avoid conflicting with that existing application.

Test the application locally
curl http://localhost:8080

If the application is running, this should return its HTML content.

Check Compose port mappings
sudo docker compose ps

Our output confirmed a mapping equivalent to:

0.0.0.0:8080->80/tcp

This means the service is published on the host's IPv4 interfaces on port 8080.

Security note: Port mapping alone does not guarantee public accessibility. AWS security group rules, routing, and other network controls also affect whether users can reach an application externally.

We did not need to change the EC2 security group to complete the local container tests.

6. Docker Compose
What is Docker Compose?

Docker Compose is a tool for defining and managing containerized applications using a YAML configuration file.

Instead of repeatedly entering a long docker run command, we can define our service in compose.yaml.

Our compose.yaml
services:
  web:
    image: my-docker-webapp:1.0
    container_name: my-docker-webapp-compose
    ports:
      - "8080:80"
    environment:
      APP_ENV: ${APP_ENV}
      APP_VERSION: ${APP_VERSION}
    restart: unless-stopped
Explanation
services: Defines the application's container services.
web: The name of our service.
image: The image used to create the container.
container_name: Sets the container's name.
ports: Maps host port 8080 to container port 80.
environment: Passes environment variables into the container.
restart: unless-stopped: Allows Docker to restart the container after many failures or daemon restarts, unless it has been explicitly stopped.
Useful Docker Compose commands

Validate the configuration:

sudo docker compose config --quiet

Start the application:

sudo docker compose up -d

Check its status:

sudo docker compose ps

View logs:

sudo docker compose logs web

Follow logs in real time:

sudo docker compose logs -f web

Press Ctrl+C to stop following the logs; this does not normally stop the container.

Stop and remove the Compose-managed container and network:

sudo docker compose down

This does not normally remove named volumes.

Rebuild the image and recreate the service:

sudo docker compose up -d --build

This is useful after changing the application or Dockerfile, although our Compose configuration currently references a prebuilt image rather than declaring a build: section. For that configuration, build the image separately before running Compose again.

7. Environment Variables and Configuration

Environment variables allow an application to receive configuration values without hardcoding them into application code.

Our .env file contains:

APP_ENV=development
APP_VERSION=1.0

Our .env.example file contains the same example settings.

Why use environment variables?

They allow configuration to differ between environments without changing the application's code.

For example:

Variable	Example value	Purpose
APP_ENV	development	Identifies the application environment
APP_VERSION	1.0	Identifies the configured application version
.env versus .env.example
.env contains the actual local configuration.
.env.example provides a template for other developers.

Our .gitignore contains:

.env
.env.*
!.env.example

This helps prevent local environment files from being committed while allowing .env.example to be tracked.

Security reminder: Environment variables are convenient for configuration, but they are not automatically a secure secret-management system. Avoid putting passwords, access tokens, or other sensitive values into Git. Use an appropriate secrets manager for real credentials.

8. Docker Volumes and Persistent Storage
What is a Docker volume?

A Docker volume provides storage managed by Docker that can persist independently of a container's lifecycle.

Without persistent storage, data written only to a container's writable layer can be lost when the container is removed.

Create a named volume
sudo docker volume create module4-learning-volume
List volumes
sudo docker volume ls
Inspect a volume
sudo docker volume inspect module4-learning-volume
Test persistence

We tested writing a file into a named volume and then reading that file from a separate container.

The important concept is:

Container 1 writes data → Container 1 exits → Container 2 reads the same data from the volume.

Our practical test confirmed that the data remained available.

Why are volumes useful?

Volumes are useful for data that should outlive an individual container, such as database files or application data.

However, volumes are not backups. Important data should also have an appropriate backup and recovery strategy.

9. Docker Networking

Docker networking allows containers to communicate with one another and with external systems.

Common Docker network types include:

Network type	Purpose
Bridge	Connects containers on a Docker bridge network
Host	Uses the host's network namespace on supported Linux configurations
None	Disables normal external container networking
Overlay	Connects containers across multiple Docker hosts in supported configurations

Docker Compose normally creates a project network for its services.

Useful networking commands

List networks:

sudo docker network ls

Inspect a network:

sudo docker network inspect docker-containerization-lab_default

The exact network name may differ if the Compose project name has been customized.

Inspect the container:

sudo docker inspect my-docker-webapp-compose

These commands help you investigate container configuration and networking.

10. Docker Security Best Practices

Security is an important part of containerization.

Do not commit secrets. Keep private .env files and credentials out of Git.
Use trusted images. Choose reputable base images and update them when necessary.
Use minimal images. Smaller images can reduce unnecessary packages and the attack surface.
Avoid unnecessary exposed ports. Publish only the ports required by the application.
Use least privilege. Avoid running containers with unnecessary privileges.
Keep Docker and its images updated. Apply security updates appropriately.
Monitor container logs. Investigate unexpected errors or suspicious activity.
Use secrets management for sensitive values. Environment variables alone are not a complete secrets solution.
Protect the Docker daemon. Access to the Docker socket can provide extensive control over the host.
Back up important persistent data. Named volumes are not a substitute for backups.
11. Troubleshooting Common Docker Problems
Problem	Possible cause	Useful command
Container exits immediately	Application error or invalid configuration	sudo docker ps -a
Port already allocated	Another process uses the host port	sudo docker ps
Webpage does not load	Container stopped or service misconfigured	sudo docker compose ps
HTTP error or blank page	Incorrect application content or web-server configuration	sudo docker compose logs web
Image not found	Image has not been built or pulled	sudo docker images
Compose configuration fails	Invalid YAML or missing variables	sudo docker compose config
Data disappears	Data was stored only in a container's writable layer	sudo docker volume ls
Git ignores a project file	A .gitignore rule matches it	git check-ignore -v <filename>
A good troubleshooting sequence

When a containerized application does not work:

Check whether the container is running.
Review the container logs.
Validate the Compose configuration.
Check the image and port mapping.
Test the application with curl.
Inspect networking and storage if needed.

This sequence helps narrow down the cause without changing unrelated resources.

12. Git and GitHub Project Management

We published our project to the existing internship repository.

Repository:
Codomax Cloud Computing & DevOps on GitHub

Module 4 project:
Docker Containerization project files

Important Git commands

Check the current branch:

git branch --show-current

Check the working tree:

git status

Stage changes:

git add Module-4/Docker-Containerization/

Review staged changes:

git diff --cached

Commit changes:

git commit -m "Update Docker containerization project"

Push changes:

git push origin main
Why use Git?

Git records changes to your project, while GitHub hosts the repository remotely and allows you to share your work.

Our project was added to the existing internship repository without replacing its previous modules.

13. Quick Revision: Important Commands

Here is a compact revision sheet.

Task	Command
Check Docker version	sudo docker --version
Check Docker service	sudo systemctl status docker
Build an image	sudo docker build -t my-docker-webapp:1.0 .
List images	sudo docker images
List running containers	sudo docker ps
List all containers	sudo docker ps -a
Start Compose application	sudo docker compose up -d
Check Compose services	sudo docker compose ps
View Compose logs	sudo docker compose logs web
Validate Compose configuration	sudo docker compose config --quiet
Test webpage	curl http://localhost:8080
List volumes	sudo docker volume ls
List networks	sudo docker network ls
Stop Compose application	sudo docker compose down
Check Git status	git status
Push to GitHub	git push origin main

Summary of What You Practised

During this module, you:

Installed and used Docker on an AWS EC2 instance.
Created a Dockerfile and built a web application image.
Ran an Nginx web application inside a container.
Configured Docker Compose.
Mapped host port 8080 to container port 80.
Used environment variables and example configuration.
Tested named-volume persistence.
Inspected container logs and networking.
Documented the project in a README.
Committed and pushed your project to GitHub.

