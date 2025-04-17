# Airflow Automation

Automates KPI and Weekly Logs scripts using Apache Airflow.

## Setup

1. Build the Docker image with `dockerfile`.
2. Run `docker-compose up`.
3. Access Airflow at [localhost:8080](http://localhost:8080/).

DAGs are in `airflow/dags` and run automatically. Keep the server running for automation.
