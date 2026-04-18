FROM python:3.13-slim

WORKDIR /app

COPY Pipfile Pipfile.lock ./
RUN pip install --no-cache-dir pipenv==2024.4.1 \
    && PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy --system

COPY src ./src
ENV PYTHONPATH=/app/src

EXPOSE 8001

CMD ["python", "-m", "user_preference_api.main"]
