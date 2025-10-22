# 1️⃣ Ingesting Clickstreams on GCP

This module simulates user interactions (click and watch events) and publishes them to **Google Pub/Sub** topics for ingestion.

## 🏗️ Architecture
**Pub/Sub → Dataflow → BigQuery → Vertex AI → Looker Studio**

## ⚙️ Setup
1. **Create Pub/Sub Topics**
   ```bash
   gcloud pubsub topics create click_events
   gcloud pubsub topics create watch_events
   ```

2. **Run Event Producers**
   ```bash
   python scripts/click_producer.py
   python scripts/watch_producer.py
   ```

3. **Validate**
   Check Pub/Sub console → Subscriptions → Messages.

## ✅ Output
Two live topics emitting real-time user activity data.
