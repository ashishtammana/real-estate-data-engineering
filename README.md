# Real Estate Data Engineering Project - Detailed README

## Overview

This project is designed as a full-fledged **end-to-end data engineering pipeline** that demonstrates modern data engineering concepts using real estate data. The project integrates multiple open-source technologies to orchestrate data extraction, transformation, storage, analysis, and visualization in a seamless workflow. The architecture is modular, scalable, and cloud-agnostic, allowing for easy deployment both locally and in the cloud.

## Purpose of the Project

The main goal of this project is to showcase the following:

- Web scraping of real estate listings.
- Storing raw and processed data in **MinIO** (S3-compatible object storage).
- Applying Change Data Capture (CDC) logic to detect and process only changed data.
- Loading and querying data efficiently with **DuckDB**.
- Orchestrating workflows with **Dagster**.
- Visualizing insights through **Apache Superset**.
- Running the entire stack using **Docker** and **Docker Compose** for easy reproducibility.

This setup is suitable for use cases such as real-time real estate market analysis, price trend monitoring, and property insights extraction.

---

## Architecture Overview

```
Web Scraping → CDC Processing → Upload to MinIO → Load with DuckDB → Data Science (Optional) → Visualization in Superset
                        ↓
                   Orchestration via Dagster
```

## Components Breakdown

### 1. **Web Scraping**
**Purpose:** Extract real estate listings from external websites.

**Why?** Web scraping is vital because most real estate data isn't provided via APIs. Scraping HTML pages allows us to extract and structure this data into CSVs for further processing.

**Technology:**
- **BeautifulSoup** and **requests** for scraping.
- Stores scraped data as CSV files.

**Output:** Raw property data (like prices, locations, features) in CSV format.

---

### 2. **Change Data Capture (CDC)**
**Purpose:** Detect if a scraped record is new, updated, or unchanged.

**Why?** Prevent redundant data uploads and processing by checking if a property listing already exists or has been updated.

**How:**
- Fingerprinting properties based on unique attributes (ID, price, etc.).
- Comparing fingerprints of newly scraped data with existing data in MinIO.

**Output:** Only new or modified records proceed further into the pipeline.

---

### 3. **MinIO (S3-Compatible Storage)**
**Purpose:** Acts as the object storage system for all CSV files.

**Why MinIO?**
- Works like AWS S3 but runs locally or on any infrastructure.
- Avoids cloud vendor lock-in.
- Provides a clean interface and browser-based UI.

**Usage:**
- Stores raw and processed CSV files.
- Buckets organize datasets (e.g., `raw-data`, `processed-data`).

---

### 4. **DuckDB**
**Purpose:** Local OLAP database engine to process CSV data.

**Why DuckDB?**
- Ideal for analytical queries on CSV and Parquet files.
- Runs in-process (no separate server needed).
- Compatible with Pandas and modern data science tools.

**Usage:**
- Loads data from MinIO.
- Performs transformations and aggregations.
- Supports ad-hoc SQL queries.

---

### 5. **Dagster (Pipeline Orchestration)**
**Purpose:** Manages the complete workflow from scraping to storage and transformation.

**Why Dagster?**
- Provides modular, observable, and testable pipelines.
- Replaces traditional cron jobs with monitored, managed tasks.
- Visual UI (Dagit) for pipeline runs.

**How components interact via Dagster:**
- Step 1: Scrape → Step 2: CDC Check → Step 3: Upload to MinIO → Step 4: Process with DuckDB → Step 5: Store Results

---

### 6. **Apache Superset (Visualization)**
**Purpose:** Visualize the processed data with dashboards.

**Why Superset?**
- Open-source BI tool.
- Connects easily to DuckDB and MinIO datasets.
- Supports charts, maps, and dashboards.

**Example Use Cases:**
- Visualize average housing prices over time.
- Heatmaps of property listings.
- Track price fluctuations of properties.

---

## How Components are Connected

| Component       | Input                | Process                                 | Output                  |
|-----------------|----------------------|-----------------------------------------|-------------------------|
| Scraper        | Web pages            | Extract property details               | Raw CSV file            |
| CDC Processor  | Raw CSV + Existing   | Compare fingerprints, filter changes   | Updated CSV file        |
| MinIO          | CSV files            | Store raw and processed data           | Persistent storage      |
| DuckDB         | CSV from MinIO       | Run SQL queries and transformations    | Analysis-ready datasets |
| Superset       | DuckDB               | Query and visualize data               | Dashboards              |
| Dagster        | Orchestrates all     | Automates and monitors the entire flow | Logs and status         |

---

## Screenshots

### 1. Docker Setup
<img width="1440" alt="Screenshot 2025-03-06 at 10 58 33 AM" src="https://github.com/user-attachments/assets/c3c95b54-9b47-4e7d-94f2-9b0177c934b0" />



### 2. Dagster Pipeline Execution
<img width="1440" alt="Screenshot 2025-03-06 at 11 04 46 AM" src="https://github.com/user-attachments/assets/28919bda-e20c-4d96-933e-724353dc3eb4" />


### 3. MinIO Storage
<img width="1440" alt="Screenshot 2025-03-06 at 11 06 45 AM" src="https://github.com/user-attachments/assets/91b3a905-e9d8-4f4c-abb6-b89e9ffcbb51" />


---

## Installation and Setup

### Prerequisites
- Docker + Docker Compose
- Python 3.10+
- Virtual Environment (`venv`)

### Setup Steps

1. **Clone the Repository**
```bash
git clone https://github.com/your-repo/real-estate-data-engineering.git
cd real-estate-data-engineering
```

2. **Create Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. **Start Docker Containers**
```bash
docker-compose up -d
```

4. **Start Dagster and MinIO**
```bash
dagster-webserver -h 0.0.0.0 -p 3000
```

5. **Access the UIs:**
- Dagster: http://localhost:3000
- MinIO: http://localhost:9001
- Superset: http://localhost:8088

---

## Why this architecture?

- **Scalability:** Can run locally, on-premise, or in the cloud.
- **Modularity:** Replace any tool (e.g., switch MinIO with AWS S3).
- **Maintainability:** Clear separation of components and responsibilities.
- **Observability:** Track the whole pipeline visually through Dagster.

---

## Future Enhancements

- Integrate Delta Lake for versioned parquet storage.
- Expand Machine Learning models for price prediction.
- Automate dashboard generation in Superset.
- CI/CD setup for production deployments.

---

## Conclusion

This project demonstrates the modern data engineering lifecycle, from data extraction to analysis, using best-in-class open-source tools. It offers an ideal foundation for learning, experimenting, and extending to real-world applications such as real estate market analytics.

---

For contributions, questions, or collaborations, please connect via GitHub or LinkedIn.

