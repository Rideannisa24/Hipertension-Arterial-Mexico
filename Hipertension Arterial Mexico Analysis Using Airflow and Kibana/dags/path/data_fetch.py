import pandas as pd
from sqlalchemy import create_engine

# loading DAG
def data_fetch():
    engine = create_engine("postgresql+psycopg2://airflow:airflow@postgres:5432/airflow")
    conn = engine.connect()

    df = pd.read_sql_query("select * from table_m3", conn)

    # save to .data/ path
    df.to_csv('/opt/airflow/data/P2M3_rizqia-dewi_data_raw.csv' , sep=',', index=False)