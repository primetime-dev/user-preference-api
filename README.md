# user-preference-api

Legacy-style service with its own local CI definition.

## Local Commands

- Install dependencies: `pipenv install --dev`
- Run tests: `PYTHONPATH=src pipenv run nosetests tests/test_app.py -v`
- Start the API: `PYTHONPATH=src pipenv run python -m user_preference_api.main`
- Build the image: `docker build -t user-preference-api:dev .`
- Apply manifests individually:
  - `kubectl apply --namespace legacy-services -f k8s/deployment.yaml`
  - `kubectl apply --namespace legacy-services -f k8s/service.yaml`

## Endpoints

- `GET /`
- `GET /health`

## Pipeline

This repo keeps a local CI workflow instead of consuming the shared golden path.
It uses Pipenv, nose, and a differently shaped deploy job.
Pushes to `main` build and publish `ghcr.io/primetime-dev/user-preference-api:${GITHUB_SHA}`,
rewrite the Deployment manifest to that immutable tag inside the release workflow, and apply
the patched manifests to Kubernetes.
