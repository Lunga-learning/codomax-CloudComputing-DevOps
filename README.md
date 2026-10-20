# Linux, Networking, AWS and Terraform Learning Log — Days 6–30

This repository contains a consolidated record of my hands-on DevOps learning from Day 6 through Day 30. Each day has a distinct focus to avoid repeating the same lesson in multiple entries.

## Learning objectives
- Practise Linux administration and command-line troubleshooting.
- Understand users, groups, permissions, networking, SSH and cloud networking fundamentals.
- Learn AWS infrastructure concepts while monitoring costs.
- Build Terraform skills using variables, locals, outputs and reusable modules.

## Repository structure

```text
devops-learning-days-06-to-30/
├── README.md
├── LEARNING_NOTES_DAYS_06-30.md
└── days/
    ├── day-06.md
    ├── ...
    └── day-30.md
```

## Evidence and accuracy
These notes consolidate the lesson records available from my learning sessions. Specific command outputs are included where they were recorded. Where an exact output was not retained, the notes describe the learning objective and command examples rather than inventing a result.

## Safety and cost controls
- AWS account status previously showed the Free plan with credits and an expiry date. Balances and plan terms can change; check the AWS Billing console before further work.
- Do not assume every AWS service or resource is free.
- Terraform exercises on Days 27–30 were local-only configurations and were checked with `terraform plan`; no `terraform apply` was run for those exercises.
- Never commit AWS access keys, passwords, private SSH keys, `.env` files, Terraform state files, or other secrets to GitHub.

## Suggested GitHub publishing steps
1. Sign in to GitHub and create a new repository named `devops-learning-days-06-to-30`.
2. Choose **Public** only if you are comfortable sharing the learning notes publicly; otherwise choose **Private**.
3. Do not initialize the repository with a README if you plan to upload this folder as-is.
4. Extract the ZIP file on your computer.
5. Upload the files through GitHub's **Add file → Upload files** page, or use Git locally:
   ```bash
   git init
   git add README.md LEARNING_NOTES_DAYS_06-30.md days/
   git commit -m "Add consolidated DevOps learning notes for days 6-30"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/devops-learning-days-06-to-30.git
   git push -u origin main
   ```
6. Replace `YOUR-USERNAME` with your GitHub username. Do not paste credentials or tokens into the repository.
7. Copy the repository URL into your course submission after the upload succeeds.

## Next module
Once the repository is uploaded, save the GitHub repository URL for submission and move on to the next module.
