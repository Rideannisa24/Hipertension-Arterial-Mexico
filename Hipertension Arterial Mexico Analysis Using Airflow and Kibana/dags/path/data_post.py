import pandas as pd
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

# exporting to elasticsearch DAG
def data_post():
    es = Elasticsearch(hosts=["http://elasticsearch:9200"])

    df = pd.read_csv('/opt/airflow/data/P2M3_rizqia-dewi_data_clean.csv')
    actions = [
        {
            "_index": "table_m3",
            "_source": row.to_dict()
        }
        for i, row in df.iterrows()
    ]
    bulk(es, actions)