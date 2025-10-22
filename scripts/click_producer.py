from google.cloud import pubsub_v1
import json, time, random, datetime

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path("netflix-analytics-lab", "click_events")

while True:
    msg = {
        "user_id": random.randint(1, 1000),
        "event_ts": datetime.datetime.utcnow().isoformat(),
        "page": random.choice(["home", "details", "search"]),
        "device": random.choice(["tv", "mobile", "web"]),
        "region": random.choice(["NA", "EU", "IN"]),
        "ab_bucket": random.choice(["A", "B"])
    }
    publisher.publish(topic_path, json.dumps(msg).encode("utf-8"))
    time.sleep(1)
