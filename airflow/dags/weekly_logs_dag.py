from airflow import DAG
from airflow.operators.bash_operator import BashOperator  # type: ignore
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 1, 1),
    'depends_on_past': False,
    'email': ['husseingamal189@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    dag_id="Weekly_Logs",
    default_args=default_args,
    schedule_interval='0 11 * * 1',
    catchup=False,
)

run_logs = BashOperator(
    task_id="run_weekly_logs",
    bash_command="""
    source /path/to/venv/bin/activate
    cd /path/to/Weekly_Logs
    python logs.py
    """,
    dag=dag
)
