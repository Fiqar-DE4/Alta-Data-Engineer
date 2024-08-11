from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

# 1. Create DAG that run in every 5 hours:

with DAG(
    'Fiqar_Airflow_Task_1',
    description='Alterra Airflow Task 1',
    schedule_interval='0 */5 * * *',
    start_date=datetime(2023, 1, 1),
    catchup=False
) as dag:



# 2. Suppose we define a new task that push a variable to xcom:

    # ti = task instance
    def push_variable_to_xcom(ti=None):
        ti.xcom_push(key='job_level1', value='Data Engineer')
        ti.xcom_push(key='job_level2', value='Data Architect')
        ti.xcom_push(key='job_level3', value='Database Administrator')



# 3. How to pull multiple values at once?:

    def pull_multiple_value_once(ti=None):
        job_level1 = ti.xcom_pull(task_ids='push_variable_to_xcom', key='job_level1')
        job_level2 = ti.xcom_pull(task_ids='push_variable_to_xcom', key='job_level2')
        job_level3 = ti.xcom_pull(task_ids='push_variable_to_xcom', key='job_level3')

        print(f'print job_level variable from xcom: {job_level1}, {job_level2}, {job_level3}')

    push_variable_to_xcom = PythonOperator(
        task_id = 'push_variable_to_xcom',
        python_callable = push_variable_to_xcom
    )

    pull_multiple_value_once = PythonOperator(
        task_id = 'pull_multiple_value_once',
        python_callable = pull_multiple_value_once
    )

    push_variable_to_xcom >> pull_multiple_value_once

