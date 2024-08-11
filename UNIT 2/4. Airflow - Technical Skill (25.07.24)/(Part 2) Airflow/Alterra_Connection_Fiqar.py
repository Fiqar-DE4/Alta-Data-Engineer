from airflow import DAG
from datetime import datetime
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator

dag = DAG(
    dag_id = 'Alterra_Connection_Fiqar',
    schedule=None,
    start_date=datetime(2022, 10, 21),
    catchup=False
)
    
get_statistic = SimpleHttpOperator(
    task_id="get_statistic",
    endpoint="/statistic",
    method="GET",
    http_conn_id="gender_api_fiqar",
    log_response=True,
    dag=dag
)

identify_name = SimpleHttpOperator(
    task_id="post_name",
    endpoint="/gender/by-first-name-multiple",
    method="POST",
    data='{"country": "ID", "locale": null, "ip": null, "first_name": "Musa"}',
    http_conn_id="gender_api_fiqar",
    log_response=True,
    dag=dag
)

def my_uri():
    from airflow.hooks.base import BaseHook
    print(f"Gender API URI ", BaseHook.get_connection("gender_api_fiqar").get_uri())

print_uri = PythonOperator(
    task_id = "print_uri",
    python_callable = my_uri
    )

get_statistic >> identify_name >> print_uri