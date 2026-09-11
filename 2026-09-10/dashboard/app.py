import os

import requests
from flask import Flask, render_template_string

app = Flask(__name__)

DEVICE_API_URL = os.getenv(
    "DEVICE_API_URL",
    "http://device-api:5000/status",
)
# 환경변수 값이 있으면 DEVICE_API_URL에 할당하고, 없으면 기본값으로 http://device-api:5000/status를 할당한다.

PAGE = """
<!doctype html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>Edge 장비 상태 대시보드</title>
  <meta http-equiv="refresh" content="5">
  <style>
    body {
      max-width: 700px;
      margin: 40px auto;
      font-family: Arial, sans-serif;
      background: #f8fafc;
    }
    h1 { color: #1e3a8a; }
    .card {
      background: white;
      border-radius: 12px;
      box-shadow: 0 2px 8px #00000018;
      margin-top: 20px;
      padding: 24px;
    }
    .online { color: #15803d; font-weight: bold; }
    .error { color: #b91c1c; }
    dt { color: #64748b; margin-top: 14px; }
    dd { font-size: 1.2rem; margin-left: 0; }
  </style>
</head>
<body>
  <h1>🛰️ Edge 장비 상태 대시보드</h1>
  <p>5초마다 가상 Jetson 장비 상태를 새로 요청합니다.</p>

  <section class="card">
    {% if device %}
      <h2>{{ device["device_name"] }}</h2>
      <p class="online">● {{ device["status"] }}</p>
      <dl>
        <dt>CPU 사용률</dt>
        <dd>{{ device["cpu_usage_percent"] }}%</dd>

        <dt>메모리 사용률</dt>
        <dd>{{ device["memory_usage_percent"] }}%</dd>

        <dt>온도</dt>
        <dd>{{ device["temperature_celsius"] }}°C</dd>

        <dt>상태 보고 시각</dt>
        <dd>{{ device["reported_at"] }}</dd>
      </dl>
    {% else %}
      <h2 class="error">장비 상태를 가져올 수 없습니다.</h2>
      <p>{{ error_message }}</p>
    {% endif %}
  </section>
</body>
</html>
"""

@app.get("/")
def dashboard():
    try:
        response = requests.get(DEVICE_API_URL, timeout=2)
        response.raise_for_status()
        return render_template_string(PAGE, device=response.json())
    except requests.RequestException as error:
        return render_template_string(
            PAGE,
            device=None,
            error_message=str(error),
        )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)