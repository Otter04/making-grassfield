import random
from datetime import datetime, timezone

from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/status")
def get_status():
    return jsonify(
        {
            "device_name": "jetson-simulator-01",
            "status": "online",
            "cpu_usage_percent": random.randint(15, 85),
            "memory_usage_percent": random.randint(20, 90),
            "temperature_celsius": round(random.uniform(38.0, 72.0), 1),
            "reported_at": datetime.now(timezone.utc).isoformat(),
        }
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)