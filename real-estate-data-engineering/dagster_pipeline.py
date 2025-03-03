from dagster import job, op
import pandas as pd
import boto3

@op
def load_data():
    return pd.read_csv('./data/kc_house_data_processed.csv')

@op
def apply_cdc(df_current):
    s3 = boto3.client(
        's3',
        endpoint_url='http://localhost:9000',
        aws_access_key_id='admin',
        aws_secret_access_key='password123',
    )
    try:
        s3.download_file('real-estate-data', 'kc_house_data_processed.csv', './data/kc_house_data_previous.csv')
        df_prev = pd.read_csv('./data/kc_house_data_previous.csv')
        df_current['fingerprint'] = df_current['id'].astype(str) + "_" + df_current['price'].astype(str)
        df_prev['fingerprint'] = df_prev['id'].astype(str) + "_" + df_prev['price'].astype(str)
        changes = df_current[~df_current['fingerprint'].isin(df_prev['fingerprint'])]
        print(f"🔍 {len(changes)} changes detected.")
    except:
        changes = df_current
        print("🚀 First run, all records are new.")
    return df_current

@op
def save_and_upload(df):
    df.to_csv('./data/kc_house_data_previous.csv', index=False)
    s3 = boto3.client(
        's3',
        endpoint_url='http://localhost:9000',
        aws_access_key_id='admin',
        aws_secret_access_key='password123',
    )
    s3.upload_file('./data/kc_house_data_previous.csv', 'real-estate-data', 'kc_house_data_processed.csv')
    print("✅ Dataset updated in MinIO.")

@job
def real_estate_pipeline():
    df = load_data()
    updated_df = apply_cdc(df)
    save_and_upload(updated_df)
