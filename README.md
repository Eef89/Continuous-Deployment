# Continuous deployment

[![Run Tests](https://github.com/Eef89/Continuous-Deployment/actions/workflows/main.yml/badge.svg)](https://github.com/Eef89/Continuous-Deployment/actions/workflows/main.yml)

This project gives a solution to develop your project on a local machine and upload it to your VPS via git. This project excists out of three components.

## Components

### 1. GIT

To upload file to github, this programme uses GIT. Thereby GIT gives a solution for version control. 

### 2. Pytest via GITHUB actions 

If a upload it made to GITHUB, GITHUB actions will automatically run a test. 
In this case I used pytest. Pytest checks if the code was correct. When the code passes the test, the next actions will be taken as described in following paragraph.

### 3. SSH and deployment via GITHUB actions

When the pytest is positive, GITHUB connetcs with the VPS via SSH. For this I used GITHUB secrets. For this I used the follwing totorial: https://dev.to/knowbee/how-to-setup-continuous-deployment-of-a-website-on-a-vps-using-github-actions-54im

## Remarks

Thank you for using my product.