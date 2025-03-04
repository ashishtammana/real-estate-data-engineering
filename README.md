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

```bash
# 1️⃣ Clone the repo
git clone https://github.com/ashishtammana/real-estate-data-engineering.git
cd real-estate-data-engineering

# 2️⃣ Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# 3️⃣ Install the dependencies
pip install -r requirements.txt

# 4️⃣ Set up the environment variables
# Create a .env file in the root directory and add:
AWS_ACCESS_KEY_ID=your_minio_access_key
AWS_SECRET_ACCESS_KEY=your_minio_secret_key
MINIO_ENDPOINT=http://localhost:9000
MINIO_BUCKET=real-estate-data

# 5️⃣ Start MinIO (optional if not already running)
docker-compose up -d

# 6️⃣ Export Dagster home directory
export DAGSTER_HOME=~/dagster_home

# 7️⃣ Start Dagster services in two terminals

# Terminal 1:
dagster-daemon run

# Terminal 2:
dagster-webserver -w workspace.yaml

# 8️⃣ Open Dagster UI
# Go to:
http://localhost:3000

# 9️⃣ Trigger the pipeline
# Run real_estate_pipeline manually from the Dagster UI or wait for the daily schedule.

---

##  🎯 ✅ Output
- Takes in raw real estate data (`kc_house_data.csv`).
- Cleans and processes the data, applying **CDC (Change Data Capture)** logic to detect and update only **new or changed records**.
- Generates a cleaned output file: `kc_house_data_processed.csv`.
- Uploads the processed dataset to **MinIO** under the **`real-estate-data`** bucket.
- Schedules automated **daily runs** through **Dagster** to keep the data fresh.
- Sets the foundation to plug in:
  - 🤖 **Machine Learning models** (for future predictions).
  - 📊 **Superset dashboards** (for data visualization).

---

