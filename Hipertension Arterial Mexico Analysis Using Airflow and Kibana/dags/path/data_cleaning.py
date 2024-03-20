import pandas as pd



def data_cleaning():
     # load
    '''  Fungsi ini ditujukan untuk membersihkan data.
    output: P2M3_rizqia-dewi_data_clean.csv (data yang telah bersih)
    '''
    data = pd.read_csv("/opt/airflow/data/P2M3_rizqia-dewi_data_raw.csv") # read csv

    # filter data

    data.dropna(inplace=True) # delete missing value

    data.drop_duplicates(inplace=True) # delete duplicate data

    data.rename(columns={"FOLIO_I": "id", "sexo": "gender", "edad": "age", "concentracion_hemoglobina": "hemoglobin_concentration", 
                   "temperatura_ambiente": "ambient_temperature", "valor_acido_urico": "uric_acid_value", "valor_albumina": "albumin_value", "valor_colesterol_hdl": "hdl_cholesterol_value", 
                   "valor_colesterol_ldl": "ldl_cholesterol_value", "valor_colesterol_total": "total_cholesterol_value", "valor_creatina": "creatinine_value", "resultado_glucosa": "glucose_result",
                   "valor_insulina": "insulin_value", "valor_trigliceridos": "triglycerides_value", "resultado_glucosa_promedio": "average_glucose_result", "valor_hemoglobina_glucosilada": "glycosylated_hemoglobin_value",
                   "valor_ferritina": "Ferritin Value", "valor_folato": "Folate Value", "valor_homocisteina": "Homocysteine Value", "valor_proteinac_reactiva": "c_reactive_protein_value",
                   "valor_transferrina": "transferrin_value", "valor_vitamina_bdoce": "vitamin_b12_value", "valor_vitamina_d": "vitamin_d_value", "peso": "weight",
                   "estatura": "height", "medida_cintura": "waist_measurement", "segundamedicion_peso": "second_weight_measurement", "segundamedicion_estatura": "second_height_measurement",
                   "distancia_rodilla_talon": "knee_heel_distance", "circunferencia_de_la_pantorrilla": "calf_circumference", "segundamedicion_cintura": "second_waist_measurement", "tension_arterial": "blood_pressure",
                   "sueno_horas": "sleep_in_hours", "masa_corporal": "body_mass", "actividad_total": "total_activity", "riesgo_hipertension": "hypertension_risk"}, inplace=True)
    data['id'] = data['id'].astype(float)
    data['gender'] = data['gender'].replace('1','male').replace('2','female').astype(object)

    for i in data.columns:
        i_lower = i.lower() # change column name to lower case
        i_cleaned = i_lower.replace(' ', '_').replace('-', '_') # change space to underscore
        data.rename(columns={i: i_cleaned}, inplace=True)
        data.columns = [col.translate(i_cleaned) for col in data.columns] 
    data.to_csv('/opt/airflow/data/P2M3_rizqia-dewi_data_clean.csv', index=True) # saving the cleaned data

