# Operations Runbook — Milestone 2

## Overview
This project packages a minimal FastAPI inference service into a multi-stage Docker image and uses GitHub Actions CI/CD to test, build, and publish versioned images to Google Artifact Registry.

Service endpoints:
- `GET /health`
- `POST /predict` (JSON: `{"value": <number>}`)

---

## Dependency pinning strategy (reproducibility)
**Goal:** deterministic builds across dev/CI/production.

- Runtime dependencies are pinned to exact versions in `app/requirements.txt`.
- Test/dev dependencies are pinned separately in `app/requirements-dev.txt`.
- CI installs both runtime + dev requirements for tests.
- Docker image installs *runtime requirements only* (keeps the runtime small and reduces attack surface).

**Update process (safe):**
1. Update one dependency version at a time.
2. Run tests locally and in CI.
3. Publish a new semantic tag `vX.Y.Z`.

---

## Image optimization (size + caching)
Techniques used:
- **Multi-stage build**:
  - Builder stage installs dependencies.
  - Runtime stage copies only the installed Python packages + app code.
- **Slim base image**: `python:3.11-slim`.
- **Layer caching**: `requirements.txt` copied and installed before app code so dependency layers can be reused.
- **.dockerignore** excludes `.venv/`, tests, and git metadata.

How to check image size:
```bash
docker images | head
