# 🏆 UCL ETL Pipeline

> An end-to-end data engineering pipeline built on the UEFA Champions League 2021–22 player performance dataset.

---

## 📌 Description

This project builds a production-style ETL pipeline using Python and pandas on the UCL 2021–22 player performance dataset sourced from Kaggle. Raw data covering individual player stats — goals, assists, distance covered, minutes played and more — is extracted, cleaned, formatted and loaded into a PostgreSQL database. The final dataset is ready for Business Intelligence teams, sports analysts and UCL pundits to query and derive insights from.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.12 | Core programming language |
| pandas | Data extraction and transformation |
| PostgreSQL | Target database |
| SQLAlchemy | Database connection engine |
| psycopg2 | PostgreSQL adapter for Python |
| uv | Python package manager |

---

## 📁 Project Structure

```
ucl-etl-pipeline/
│
├── data/
│   ├── raw/                  ← Original Kaggle CSVs (untouched)
│   └── processed/            ← Cleaned data checkpoint
│       └── UCL_Processed.csv
│
├── pipeline/
│   ├── Extract.py            ← Reads raw CSVs into pandas DataFrames
│   ├── Transform.py          ← Cleans, renames, fixes dtypes
│   └── Load.py               ← Loads clean data into PostgreSQL
│
├── .gitignore
└── README.md
```

---

## ⚙️ How to Run

### 1. Clone the repo
```bash
git clone https://github.com/ijlalxansari1/ucl-etl-pipeline.git
cd ucl-etl-pipeline
```

### 2. Install dependencies
```bash
uv add pandas sqlalchemy psycopg2-binary
```

### 3. Download the dataset
Download from [Kaggle](https://www.kaggle.com/datasets/azminetoushikwasi/ucl-202122-uefa-champions-league) and place CSVs in `data/raw/`.

### 4. Set up PostgreSQL
```sql
CREATE DATABASE ucl_pipeline;
```

### 5. Run the pipeline
```bash
python pipeline/Extract.py
python pipeline/Transform.py
python pipeline/Load.py
```

---

## 📊 Sample Output

```
            PLAYER         CLUB    POSITION  MINUTES  MATCHES  GOALS  ASSISTS  DISTANCE(KM)
0         Courtois  Real Madrid  Goalkeeper     1230       13      0        0          64.2
1  Vinícius Júnior  Real Madrid     Forward     1199       13      4        6         133.0
2          Benzema  Real Madrid     Forward     1106       12     15        1         121.5
3           Modrić  Real Madrid  Midfielder     1077       13      0        4         124.5
4     Éder Militão  Real Madrid    Defender     1076       12      0        0         110.4
```

---

## 👤 Author

**Ijlal** — Data Engineer in progress
- GitHub: [@ijlalxansari1](https://github.com/ijlalxansari1)
- Portfolio: [dataden.vercel.app](https://dataden.vercel.app)
