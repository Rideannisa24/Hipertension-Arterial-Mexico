-- SQLBook: Code
-- Active: 1704110531772@@localhost@5432@airflow
CREATE TABLE IF NOT EXISTS table_m3 (
    FOLIO_I object PRIMARY KEY,
	sexo int,
	edad int,
	concentracion_hemoglobina float,
	temperatura_ambiente int,
	valor_acido_urico float,
	valor_albumina float,
	valor_colesterol_hdl int,
	valor_colesterol_ldl float,
	valor_colesterol_total int,
    valor_creatina float,
	resultado_glucosa float,
	valor_insulina float,
	valor_trigliceridos int,
	resultado_glucosa_promedio int,
	valor_hemoglobina_glucosilada float,
	valor_ferritina float,
	valor_folato float,
	valor_homocisteina float,
	valor_proteinac_reactiva float,
	valor_transferrina float,
	valor_vitamina_bdoce float,
	valor_vitamina_d float,
	peso float,
	estatura float,
	medida_cintura float,
	segundamedicion_peso float,
	segundamedicion_estatura float,
	distancia_rodilla_talon float,
	circunferencia_de_la_pantorrilla float,
	segundamedicion_cintura float,
	tension_arterial int,
	sueno_horas int,
    masa_corporal float,
    actividad_total int,
    riesgo_hipertension int
);
-- SQLBook: Code
-- Active: 1704110531772@@localhost@5432@airflow
COPY public.table_m3 FROM 'C:/Users/Rizqia Dewi Annisa/Hacktiv8/p2-ftds010-hck-m3-Rideannisa24/P2M3_rizqia-dewi_data_raw.csv' 
DELIMITER ',' 
CSV HEADER;
-- SQLBook: Code
-- Active: 1698374986638@@127.0.0.1@5432@postgres
 # import libraries
import psycopg2 as psy
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('postgresql://postgre:240697@localhost:5434/airflow')
data = pd.read_csv('airflow/dags/P2M3_rizqia-dewi_data_raw.csv')

data.reset_index(drop=True, inplace=True)
data.to_sql('table_m3', engine, if_exists='replace', index=True)



-- SQLBook: Code
# connect to location postgresql
db_connection_str = 'postgresql://airflow:airflow@localhost:5434/airflow'
engine = create_engine(db_connection_str)
-- SQLBook: Code
# CSV file path
csv_file_path = 'Superstore.csv'

# Read CSV into a DataFrame with 'latin-1' encoding
data = pd.read_csv(csv_file_path, encoding='latin-1')

# Write DataFrame to PostgreSQL
data.to_sql('table_m3', engine, if_exists='replace', index=False)