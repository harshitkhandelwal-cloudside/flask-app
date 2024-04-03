FROM python:3.9-slim
ENV DOCKER_BUILDKIT=0
ENV COMPOSE_DOCKER_CLI_BUILD=0
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD  NEW_RELIC_CONFIG_FILE=./newrelic.ini newrelic-admin run-program gunicorn -w 4 -b 0.0.0.0:5000 app:app --access-logfile - --error-logfile -

