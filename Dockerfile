FROM FROM python:3.8-bullseye
ENV DOCKER_BUILDKIT=0
ARG MAX_THREADS=4096
RUN echo "DefaultLimitNPROC=$MAX_THREADS" >> /etc/systemd/system.conf
ENV COMPOSE_DOCKER_CLI_BUILD=0
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD  NEW_RELIC_CONFIG_FILE=./newrelic.ini newrelic-admin run-program gunicorn -w 4 -b 0.0.0.0:5000 app:app --access-logfile - --error-logfile -

