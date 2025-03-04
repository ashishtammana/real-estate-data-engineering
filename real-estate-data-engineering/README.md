Real Estate Data Engineering Project

Overview

This project is an end-to-end Real Estate Data Engineering pipeline featuring:

✅ Web-scraping/CSV ingestion

✅ Change Data Capture (CDC) logic

✅ Uploading to MinIO (S3 compatible)

✅ Daily scheduled runs with Dagster

✅ Future-proof for machine learning, Superset dashboards, and more!

Tech Stack

Python

Postgres

Docker

Dagster

MinIO

Pandas

SQLAlchemy

Apache Superset

Setup Instructions

Clone the repository:

git clone https://github.com/ashishtammana/real-estate-data-engineering.git
cd real-estate-data-engineering

Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Create a .env file with:

AWS_ACCESS_KEY_ID=your_minio_access_key
AWS_SECRET_ACCESS_KEY=your_minio_secret_key
MINIO_ENDPOINT=http://localhost:9000
MINIO_BUCKET=real-estate-data

Start MinIO (optional):

docker-compose up -d

Export Dagster home directory:

export DAGSTER_HOME=~/dagster_home

Start Dagster services in two terminals:

dagster-daemon run
dagster-webserver -w workspace.yaml

Access Dagster UI at:
http://localhost:3000

(Optional) Install and set up Superset:
Follow the Superset installation guide to create dashboards on processed data.

Folder Structure

/data
/scripts
/notebooks
/reports

Sample Output

Processes raw real estate data (kc_house_data.csv).

Applies CDC logic to detect changes.

Outputs kc_house_data_processed.csv.

Uploads to MinIO under real-estate-data bucket.

Automated daily runs with Dagster.

Data ready for visualization in Superset dashboards.
