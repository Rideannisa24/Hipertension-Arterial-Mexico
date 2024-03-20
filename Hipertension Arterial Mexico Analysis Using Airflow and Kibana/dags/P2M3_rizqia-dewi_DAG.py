'''
==============================================================================
Milestone 3

Nama  : Rizqia Dewi Annisa
Batch : FTDS HCK-010

Program ini dibuat untuk melakukan automatisasi transform dan load data dari PostgreSQL ke ElasticSearch. Adapun dataset yang dipakai adalah dataset mengenai Hipertension Arterial Mexico (Resiko Tekanan Darah Tinggi Masyarakat Mexico) Tahun 2022.
===============================================================================
'''

# import ;ibrary
import datetime as dt
from airflow import DAG
from airflow.operators.python import PythonOperator

from path.data_fetch import data_fetch
from path.data_cleaning import data_cleaning
from path.data_post import data_post

from datetime import datetime
from sqlalchemy import create_engine, insert
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


default_args = {
    'owner': 'rizqia',
    'start_date': datetime(2024, 1, 2)
}

with DAG(
    'ETL',
    default_args=default_args,
    schedule_interval='30 6 * * *', # schedule for 6:30 AM WIB
    ) as dag:
    
    data_fetch = PythonOperator(
        task_id='Fetch_from_Postgresql',
        python_callable=data_fetch
    )

    data_cleaning = PythonOperator(
        task_id='Data_Cleaning',
        python_callable=data_cleaning
    )

    data_post = PythonOperator(
        task_id='Post_to_Elasticsearch',
        python_callable=data_post
    )

    # order of execution
    data_fetch >> data_cleaning >> data_post


