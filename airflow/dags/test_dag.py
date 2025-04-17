from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
import requests



def print_welcome():
    print('Welcome to Airflow!')




dag = DAG(
    'test_dag',
    default_args={'start_date': days_ago(1)},
    schedule_interval='0 22 * * *',
    catchup=False
)



print_welcome_task = PythonOperator(
    task_id='print_welcome',
    python_callable=print_welcome,
    dag=dag
)

