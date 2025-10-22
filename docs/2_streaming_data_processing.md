# 2️⃣ Streaming Data Processing with Dataflow

This stage uses **Google Dataflow** to stream Pub/Sub data into **BigQuery**.

## 🧩 Objective
Stream raw click/watch events into BigQuery `raw` tables.

## ⚙️ Steps
1. Create BigQuery Dataset:
   ```bash
   bq mk --dataset netflix-analytics-lab:raw
   ```

2. Deploy Dataflow Template: *Pub/Sub → BigQuery*
   - Input: `click_events`, `watch_events`
   - Output: `raw.click_events`, `raw.watch_events`

3. Validate:
   ```sql
   SELECT * FROM `netflix-analytics-lab.raw.click_events` LIMIT 10;
   ```

## ✅ Output
Continuous ingestion from Pub/Sub → BigQuery.
