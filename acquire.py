import pandas as pd
import numpy as np
import os
from env import host, username, password, get_db_url


def titanic():
    sql = 'SELECT * FROM passengers'
    df = pd.read_sql(sql, get_db_url('titanic_db'))
    return df

def get_titanic_data():
    
    sql = 'SELECT * FROM passengers'

    if os.path.isfile('titanic_df.csv'):
        return pd.read_csv('titanic_df.csv', index_col=0)
        
    else:
        df = pd.read_sql(sql, get_db_url('titanic_db'))
        df.to_csv('titanic_df.csv')
        return df

def iris():
    sql = """
                SELECT
                species_id,
                species_name,
                sepal_length,
                sepal_width,
                petal_length,
                petal_width
                FROM measurements
                JOIN species USING(species_id)
                """
    df = pd.read_sql(sql, get_db_url('iris_db'))
    return df

def get_iris_data():
    sql = """
                SELECT
                species_id,
                species_name,
                sepal_length,
                sepal_width,
                petal_length,
                petal_width
                FROM measurements
                JOIN species USING(species_id)
                """
    if os.path.isfile('iris_df.csv'):
        return pd.read_csv('iris_df.csv', index_col=0)
        
    else:
        df = pd.read_sql(sql, get_db_url('iris_db'))
        df.to_csv('iris_df.csv')
        return df

def telco():

    sql = """
                select * from customers
                join contract_types using (contract_type_id)
                join internet_service_types using (internet_service_type_id)
                join payment_types using (payment_type_id)
                """
    df = pd.read_sql(sql, get_db_url('telco_churn'))
    return df

def get_telco_data():
    sql = """
             select * from customers
             join contract_types using (contract_type_id)
             join internet_service_types using (internet_service_type_id)
             join payment_types using (payment_type_id)
              """
    if os.path.isfile('telco.csv'):
        return pd.read_csv('telco.csv', index_col=0)
    
    else:
        df = pd.read_sql(sql,get_db_url('telco_churn'))
        df.to_csv('telco.csv')
        return df
