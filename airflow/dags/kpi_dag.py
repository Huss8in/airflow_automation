from airflow import DAG
from airflow.operators.python_operator import PythonOperator  # type: ignore
from datetime import datetime, timedelta
from KPI_Weekly_Report.kpi import main


def kpi():
    main()


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

dag = DAG(
    dag_id="kpi_weekly_report",
    default_args=default_args,
    schedule_interval="0 11 * * 1",
    catchup=False,
)

kpi_task = PythonOperator(
    task_id="kpi_weekly_report_task", python_callable=kpi, dag=dag
)
