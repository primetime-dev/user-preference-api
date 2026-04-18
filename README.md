# user-preference-api

Legacy-style service with its own local CI definition.

## Local Commands

- Install dependencies: `pipenv install --dev`
- Run tests: `PYTHONPATH=src pipenv run python -m unittest -v tests/test_app.py`
- Start the API: `PYTHONPATH=src pipenv run python -m user_preference_api.main`
- Build the image: `docker build -t user-preference-api:dev .`
- Apply manifests individually:
  - `kubectl apply --namespace legacy-services -f k8s/deployment.yaml`
  - `kubectl apply --namespace legacy-services -f k8s/service.yaml`

## Quick Start

Start the service directly:

```bash
pipenv install --dev
PYTHONPATH=src pipenv run python -m user_preference_api.main
```

In another terminal, verify it is serving traffic:

```bash
curl http://127.0.0.1:8001/
curl http://127.0.0.1:8001/health
```

Build and run the container:

```bash
docker build -t user-preference-api:dev .
docker run --rm -p 8001:8001 user-preference-api:dev
```

Then verify the containerized service:

```bash
curl http://127.0.0.1:8001/
curl http://127.0.0.1:8001/health
```

## Endpoints

- `GET /`
- `GET /health`

## Pipeline

This repo keeps a local CI workflow instead of consuming the shared golden path.
It uses Pipenv, the standard library test runner, and a differently shaped deploy job.
Pushes to `main` build and publish `ghcr.io/primetime-dev/user-preference-api:${GITHUB_SHA}`,
rewrite the Deployment manifest to that immutable tag inside the release workflow, and apply
the patched manifests to Kubernetes.
