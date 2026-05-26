from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

##Create configuration DAG owner as mardigtx, define start schedule, and no retries when fail
default_args = {
    "owner": "mardigtx",
    "start_date": datetime(2024, 11, 1),
    "retries": 0
}

with DAG(
    dag_id="P2M3_Mardi_Wicaksana_DAG",
    default_args=default_args,
    schedule_interval='10-30/10 9 * * 6',
    catchup=False) as dag:

    #Calling task extract.py
    extract = BashOperator(task_id="extract",bash_command="sudo -u airflow python /opt/airflow/scripts/extract.py")
    #calling task transform.py
    transform = BashOperator(task_id="transform", bash_command="sudo -u airflow python /opt/airflow/scripts/transform.py")
    #calling task load.py
    load = BashOperator(task_id="load", bash_command="sudo -u airflow python /opt/airflow/scripts/load.py")

    #Define the workflow airflow process step by step
    extract >> transform >> load