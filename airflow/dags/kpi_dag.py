from airflow import DAG
from airflow.operators.bash_operator import BashOperator # type: ignore
from datetime import datetime, timedelta
from KPI_Weekly_Report.kpi import main
# ---------------------------------- #
def kpi():
    main()
# ---------------------------------- #
default_args = {
    "owner": "airflow",
    "start_date": datetime(2025, 1, 1),
    "depends_on_past": False,
    "email": ["husseingamal189@gmail.com"],
    "email_on_failure": True,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}
# ---------------------------------- #
dag = DAG(
    dag_id="kpi_weekly_report",
    default_args=default_args,
    schedule_interval="0 11 * * 1",
    catchup=False,
)
# ---------------------------------- #
# https://airflow.apache.org/docs/apache-airflow/stable/howto/operator/bash.html
run_kpi = BashOperator(
    task_id='run_kpi_script',
    bash_command='source KPI_Weekly_Report/venv/bin/activate && cd airflow/dags/KPI_Weekly_Report && python kpi.py',
    dag=dag
)
