from airflow import DAG
from airflow.providers.odbc.hooks.odbc import OdbcHook 
from airflow.providers.microsoft.mssql.operators.mssql import MsSqlOperator
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.bash import BashOperator
from airflow.providers.papermill.operators.papermill import PapermillOperator
# from airflow.providers.postgres.hooks.postgres import PostgresHook

from datetime import datetime, timedelta
import json
from pandas import json_normalize

notebook = "transform_chat"

# DAG
with DAG(
    'twitch_refine_messages',
    start_date=datetime(2024,1,1),
    schedule_interval='@daily',
    catchup=False
) as dag:
    create_output_folder = BashOperator(
        task_id="create_output_folder",
        bash_command="mkdir -p /usr/local/spark/app/"+notebook
    )
    
    refine_messages = PapermillOperator(
        task_id="run_notebook_test",
        input_nb="/usr/local/spark/app/"+notebook+".ipynb",
        output_nb="/usr/local/spark/app/"+notebook+"/{{ execution_date }}.ipynb",
        parameters={"msgs": "Ran from Airflow at {{ execution_date }}!"}
    )

    # Dependencies
    create_output_folder >> refine_messages