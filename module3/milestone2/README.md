# Milestone 2 - Containerization & CI/CD

[![CI](https://github.com/sonthenguyen/mlops-module3/actions/workflows/build.yml/badge.svg)](https://github.com/sonthenguyen/mlops-module3/actions/workflows/build.yml)

## What this is
A minimal ML inference API containerized with Docker and deployed via CI/CD to Google Artifact Registry.

## Run locally (Docker)
```bash
cd module3/milestone2
docker build -t ml-service:v0.1.0 .
docker run --rm -p 8000:8000 ml-service:v0.1.0
```
