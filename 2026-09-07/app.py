import json
from datetime import datetime
from pathlib import Path

from flask import Flask, redirect, render_template_string, request

app = Flask(__name__)
#study_logs = []   #이전 2026-09-04 폴더에서의 파일에서는 이런식으로 파일 내부의 리스트에 저장시켜
#컨테이너가 종료되었을때 기록이 남지 않았다. 

DATA_PATH = Path("/data/study_logs.json")

PAGE = """
<!doctype html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>Docker 학습 기록</title>
  <style>
    body {
      max-width: 720px;
      margin: 40px auto;
      font-family: Arial, sans-serif;
      line-height: 1.6;
    }
    input, textarea, button {
      box-sizing: border-box;
      width: 100%;
      padding: 10px;
      margin: 6px 0 14px;
    }
    button {
      background: #2563eb;
      border: 0;
      color: white;
      cursor: pointer;
    }
    article {
      border: 1px solid #ddd;
      border-radius: 8px;
      margin: 12px 0;
      padding: 14px;
    }
    .time {
      color: #666;
      font-size: 0.85rem;
    }
  </style>
</head>
<body>
  <h1>🐳 Docker 학습 기록</h1>
  <p>Docker 볼륨에 기록을 저장하는 웹앱입니다.</p>

  <form method="post">
    <label for="title">오늘 배운 주제</label>
    <input id="title" name="title" required>

    <label for="content">학습 내용</label>
    <textarea id="content" name="content" rows="4" required></textarea>

    <button type="submit">기록 추가</button>
  </form>

  <h2>기록 목록</h2>

  {% if study_logs %}
    {% for log in study_logs %}
      <article>
        <strong>{{ log["title"] }}</strong>
        <div>{{ log["content"] }}</div>
        <div class="time">{{ log["created_at"] }}</div>
      </article>
    {% endfor %}
  {% else %}
    <p>아직 작성한 기록이 없습니다.</p>
  {% endif %}
</body>
</html>
"""

def load_study_logs():
    if not DATA_PATH.exists():
        return []

    return json.loads(DATA_PATH.read_text(encoding="utf-8"))

def save_study_logs(study_logs):
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    DATA_PATH.write_text(
        json.dumps(study_logs, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

@app.route("/", methods=["GET", "POST"])
def index():
    study_logs = load_study_logs()

    if request.method == "POST":
        study_logs.insert(
            0,
            {
                "title": request.form["title"],
                "content": request.form["content"],
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            },
        )
        save_study_logs(study_logs)
        return redirect("/")

    return render_template_string(PAGE, study_logs=study_logs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)