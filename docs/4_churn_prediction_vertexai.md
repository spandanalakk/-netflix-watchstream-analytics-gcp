# 4️⃣ Churn Prediction with Vertex AI AutoML

Train a no-code ML model in **Vertex AI AutoML**.

## ⚙️ Steps
1. Import data from BigQuery (`gold.user_engagement_daily`).
2. Target column: `churn_label`.
3. Train classification model (max node hours = 1).
4. Generate batch predictions to `gold.predictions_user_churn`.

## 🔍 Validation
```sql
SELECT user_id, churn_label, predicted_churn_label
FROM `netflix-analytics-lab.gold.predictions_user_churn`
LIMIT 10;
```

## ✅ Output
Vertex AI AutoML model predicts churn probability.
