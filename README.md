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
