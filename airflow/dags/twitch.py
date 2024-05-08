from airflow import DAG
from airflow.providers.odbc.hooks.odbc import OdbcHook 
from airflow.providers.microsoft.mssql.operators.mssql import MsSqlOperator
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator
# from airflow.providers.postgres.hooks.postgres import PostgresHook

from datetime import datetime, timedelta
import json
from pandas import json_normalize

# DAG
with DAG(
    'twitch_refine_messages',
    start_date=datetime(2024,1,1),
    schedule_interval='@daily',
    catchup=False
) as dag:
    insert_into_table1 = MsSqlOperator(
        task_id='test_task1',
        mssql_conn_id='mssql',
        sql='''
        USE DataAnalytics
        INSERT INTO Twitch.MessagesRef
        VALUES (0, GETDATE(), 'test','PRIVMSG','test','worked!',0)
        ''',
    )

    insert_into_table2 = MsSqlOperator(
        task_id='test_task2',
        mssql_conn_id='mssql',
        sql='''
        USE DataAnalytics
        INSERT INTO Twitch.MessagesRef
        VALUES (0, GETDATE(), 'test','PRIVMSG','test','worked 2!',0)
        ''',
    )

    # is_api_available = HttpSensor(
    #     task_id = 'is_api_available',
    #     http_conn_id='user_api',
    #     endpoint='api/',
    # )

    # extract_employee = SimpleHttpOperator(
    #     task_id='extract_employee',
    #     http_conn_id='user_api',
    #     endpoint='api/',
    #     method='GET',
    #     response_filter=lambda response: json.loads(response.text),
    #     log_response=True #See response in UI
    # )

    # process_employee = PythonOperator(
    #     task_id='process_employee',
    #     python_callable=_process_employee
    # )

    # store_employee = PythonOperator(
    #     task_id='store_employee',
    #     python_callable=_store_employee
    # )

    # Dependencies
    insert_into_table1 >> insert_into_table2

# Aux Functions
def _process_employee(ti):
    employee = ti.xcom_pull(task_ids="extract_employee")
    employee = employee['results'][0]
    processed_employee = json_normalize({
        'firstname': employee['name']['first'],
        'lastname': employee['name']['last'],
        'country': employee['location']['country'],
        'username': employee['login']['username'],
        'password': employee['login']['password'],
        'email': employee['email'],
    })
    processed_employee.to_csv('/tmp/processed_employee.csv', index=None, header=False)

def _store_employee():
    hook = PostgresHook(postgres_conn_id = 'postgres')
    hook.copy_expert(
        sql = '''
            COPY Employee FROM stdin WITH DELIMITER AS ',';
        ''',
        filename='/tmp/processed_employee.csv',
    )