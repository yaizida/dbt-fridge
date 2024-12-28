from airflow import DAG
from airflow.decorators import task
from airflow.datasets import Dataset
from datetime import datetime

my_dataset = Dataset("postgresql://user:password@localhost:5432/mydatabase?table=my_table")

with DAG(
    dag_id='consumer_dag',
    start_date=datetime(2024, 1, 1),
    schedule=[my_dataset],  # Triggered when the dataset is updated
    catchup=False,
) as dag:

    @task
    def process_data(**context):
        triggering_dataset_events = context['triggering_dataset_events']
        print("Triggered by dataset events:", triggering_dataset_events)

    process_data()
