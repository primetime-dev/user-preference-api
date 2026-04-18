FROM python:3.13-slim

WORKDIR /app

COPY Pipfile Pipfile.lock ./
RUN pip install --no-cache-dir pipenv \
    && PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy --system

COPY src ./src
ENV PYTHONPATH=/app/src

EXPOSE 8001

CMD ["flask", "--app", "user_preference_api.main:app", "run", "--host=0.0.0.0", "--port=8001"]
