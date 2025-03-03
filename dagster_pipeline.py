import os
import pandas as pd
import boto3
from dagster import job, op, ScheduleDefinition, Definitions

# MinIO Config
MINIO_URL = "http://localhost:9000"
MINIO_ACCESS_KEY = "admin"
MINIO_SECRET_KEY = "password123"
BUCKET_NAME = "real-estate-data"
CSV_PATH = "data/kc_house_data_processed.csv"

# Load CSV data
@op
def load_data():
    df = pd.read_csv(CSV_PATH)
    return df

# Apply CDC logic
@op
def apply_cdc(df):
    df['fingerprint'] = df['id'].astype(str) + df['price'].astype(str)
    return df

# Upload processed data to MinIO
@op
def upload_to_minio(df):
    session = boto3.session.Session()
    client = session.client(
        's3',
        endpoint_url=MINIO_URL,
        aws_access_key_id=MINIO_ACCESS_KEY,
        aws_secret_access_key=MINIO_SECRET_KEY,
    )

    csv_buffer = df.to_csv(index=False).encode()
    client.put_object(Bucket=BUCKET_NAME, Key="processed_properties.csv", Body=csv_buffer)
    print("✅ Uploaded processed data to MinIO.")

# Define the full real estate pipeline
@job
def real_estate_pipeline():
    df = load_data()
    processed_df = apply_cdc(df)
    upload_to_minio(processed_df)

# Schedule to run daily at midnight
daily_schedule = ScheduleDefinition(
    job=real_estate_pipeline,
    cron_schedule="0 0 * * *",
)

# Register the job and schedule
defs = Definitions(
    jobs=[real_estate_pipeline],
    schedules=[daily_schedule],
)
