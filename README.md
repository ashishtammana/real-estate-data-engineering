# 🏡 Real Estate Data Engineering Pipeline

This project is an end-to-end **real estate data pipeline** built with **Dagster**, featuring:

✅ Web-scraping/CSV ingestion  
✅ Change Data Capture (CDC) logic  
✅ Uploading to **MinIO** (S3 compatible)  
✅ Daily scheduled runs with **Dagster**  
✅ Future-proof for machine learning, Superset dashboards, and more!

---

## 🚀 Tech Stack
- 🏗️ **Dagster** – Orchestration & scheduling
- 🧺 **MinIO** – Object storage (S3 compatible)
- 📊 **Pandas** – Data processing
- ☁️ **Boto3** – Upload to MinIO
- 🐳 **Docker** – For MinIO local setup (optional)
- 🔄 **CDC** – Detect changes and update data

---

## 🔧 How to Run

### 1️⃣ Clone the repo
```bash
git clone https://github.com/ashishtammana/real-estate-data-engineering.git
cd real-estate-data-engineering

### 2️⃣ Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate

### 3️⃣ Install the requirements
```bash
pip install -r requirements.txt

### 4️⃣ Set up Dagster environment
export DAGSTER_HOME=~/dagster_home
mkdir -p $DAGSTER_HOME

### 5️⃣ Start MinIO (optional if not already running)
```bash
docker-compose up -d

###6️⃣ Export Dagster home directory
```bash
export DAGSTER_HOME=~/dagster_home

###7️⃣ Start Dagster services
Open two terminals:
Terminal1:
```bash
dagster-daemon run
Terminal2:
```bash
dagster-webserver -w workspace.yaml

###8️⃣ Open Dagster UI
Go to http://localhost:3000

###9️⃣ Trigger the pipeline
Run real_estate_pipeline manually or wait for the daily schedule.

###✅ Output
Cleaned data with CDC applied.
Processed dataset uploaded to MinIO.
Automated daily updates.


###Folder Structure
zreal-estate-data-engineering/
│
├── data/
│   ├── kc_house_data.csv
│   └── kc_house_data_processed.csv
│
├── dagster_pipeline.py
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .env

