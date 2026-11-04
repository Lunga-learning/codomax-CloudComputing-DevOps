# DevOps Project Tracker — CI/CD Pipeline

## 1. Overview

The Module 6 GitHub Actions workflow automates testing, container image building, and deployment of the Flask application.

Workflow file: `.github/workflows/module6-ci.yml`

The existing Module 5 workflow is separate and remains unchanged.

## 2. Workflow Triggers

The workflow runs when:

- Code is pushed to the `main` branch and changes affect `Module-6-Capstone/**` or the workflow file.
- A pull request targets `main` and changes affect those paths.
- The workflow is started manually using `workflow_dispatch`.

## 3. Continuous Integration – Test Job

The test job runs on `ubuntu-latest`.

Results:

1. Checks out the repository.
2. Sets up Python 3.12.
3. Installs the development dependencies from ` requirements-dev.txt` .
4. Runs the automated test suite with coverage:
   `python -m pytest --cov=app --cov-report=term-missing`
5. Builds the Docker image:
   `docker build -t devops-project-tracker:ci .`

A failure in the test job prevents the deployment job from running.

## 4. Test Results

The local test run completed successfully:

- Tests collected: 13
0- Tests passed: 13
- Tests failed: 0
- Total application test coverage: 75%
- Local Python version: 3.14.4
- CI Python version: 3.12

Coverage by module in the local run:

\ | Module | Coverage |
\ | === | ===: |
| `app/__init__.py` | 49% |
| `app/auth.py` | 78% |
| `app/models.py` | 92% |
| `app/projects.py` | 89% |
| `app/tasks.py` | 82% |
| **Total** | **75%** |

The CI workflow uses Python 3.12, while the recorded local test run used Python 3.14.4.

## 5. Continuous Deployment – Deploy Job

The deploy job:

- Depends on successful completion of the test job.
- Runs only for a push to `main`.
- Uses a concurrency group to prevent overlapping Module 6 deployments.
- Connects to the existing EC2 host using SSH.
- Transfers a compressed archive of the application files.
- Extracts the archive in the application directory on EC2.
- Validates the production Docker Compose configuration.
- Rebuilds and restarts only the application service.
- Polls the local `/health` endpoint to verify deployment.

The deployment uses `docker compose ... up -d --build --no-deps web`. The `--no-deps` option avoids recreating dependent services, including the separately hosted Aurora database.

## 6. Deployment Security

The workflow uses GitHub Actions secrets for the EC2 connection details:

- `EC_HOST`
- `EC_SSH_KEY`

Secret values are not stored in the repository or printed in this documentation.

The workflow starts an SSH agent, obtains the EC2 SSH host key, and checks its EDv�} fingerprint against the expected fingerprint before transferring files.

The production `.env.aws` file and `docker-compose.aws.yml` file are maintained on the EC2 host. The deployment verifies that these files exist before proceeding.

## 7. Deployment Health Verification

After restarting the application, the workflow checks:

`http://127.0.0.1:5000/health`

It retries the health check up to 12 times, waiting 5 seconds between attempts. If the application does not become healthy, the deployment job fails.

Expected response:

```json
{"status": "healthy"}
```

## 8. Deployment Flow

### Deployment Flow

``mermaid
flowchart TD

    A[Push to main] --> B[GitHub Actions]
    B --> C[Install Python 3.12 dependencies]
    C --> D[Run pytest with coverage]
    D --> E[Build Docker image]
    E --> F{Tests and build successful?}
    F -- No --> G[Stop workflow]
    F -- Yes --> H[Start SSH agent]
    H --> I[Verify EC2 host fingerprint]
    I --> J[Transfer application archive]
    J --> K[Extract files on EC2]
    K --> L[Validate production Compose config]
    L --> M[Rebuild and restart web service]
    M --> N[Poll health endpoint]
    N --> O[Deployment successful]
```

## 9. Operational Notes

- Pull requests run the CI test and image-build job but do not deploy.
- Deployment is restricted to pushes to `main` after the test job succeeds.
- The workflow deploys application files; it does not provision or destroy AWS infrastructure.
- Aurora PostgreSQL is managed separately and is not recreated by the application deployment.
- Keep GitHub Actions secrets private and rotate them if they are exposed.
