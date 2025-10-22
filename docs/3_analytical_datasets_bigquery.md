# 3️⃣ Analytical Datasets in BigQuery

Transform raw data into structured insights across **Raw → Processed → Gold** layers.

## ⚙️ Steps

### 1. Processed Layer
```bash
bq query --use_legacy_sql=false < sql/processed_watch_sessions.sql
```

### 2. Gold Layer
```bash
bq query --use_legacy_sql=false < sql/gold_user_engagement_daily.sql
```

## 🔍 Validation
```sql
SELECT * FROM `netflix-analytics-lab.gold.user_engagement_daily` LIMIT 10;
```

## ✅ Output
Sessionized and feature-rich datasets ready for ML.
