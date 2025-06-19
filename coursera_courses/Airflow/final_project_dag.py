from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# Task 1.1: Define DAG arguments
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Task 1.2: Define the DAG
with DAG(
    dag_id='final_project_dag',
    default_args=default_args,
    description='Final project DAG for ETL process using BashOperator',
    schedule_interval='@daily',
    catchup=False
) as dag:

    # Task 2.1: Unzip data
    unzip_data = BashOperator(
        task_id='unzip_data',
        bash_command='unzip /home/airflow/data/archive.zip -d /home/airflow/data/extracted'
    )

    # Task 2.2: Extract from CSV
    extract_csv = BashOperator(
        task_id='extract_csv',
        bash_command='cut -d"," -f1,2 /home/airflow/data/extracted/file.csv > /home/airflow/data/staging/csv_data.csv'
    )

    # Task 2.3: Extract from TSV
    extract_tsv = BashOperator(
        task_id='extract_tsv',
        bash_command='cut -f5,6 /home/airflow/data/extracted/file.tsv > /home/airflow/data/staging/tsv_data.csv'
    )

    # Task 2.4: Extract from fixed-width file
    extract_fixed_width = BashOperator(
        task_id='extract_fixed_width',
        bash_command='cut -c 10-20,30-40 /home/airflow/data/extracted/file.txt > /home/airflow/data/staging/fixed_width_data.csv'
    )

    # Task 2.5: Consolidate data
    consolidate_data = BashOperator(
        task_id='consolidate_data',
        bash_command='paste -d"," /home/airflow/data/staging/csv_data.csv /home/airflow/data/staging/tsv_data.csv /home/airflow/data/staging/fixed_width_data.csv > /home/airflow/data/staging/consolidated.csv'
    )

    # Task 2.6: Transform the data
    transform_data = BashOperator(
        task_id='transform_data',
        bash_command='awk \'BEGIN{FS=OFS=","} { $1=toupper($1); print }\' /home/airflow/data/staging/consolidated.csv > /home/airflow/data/staging/transformed.csv'
    )

    # Task 2.7: Define task pipeline
    unzip_data >> extract_csv >> extract_tsv >> extract_fixed_width >> consolidate_data >> transform_data
