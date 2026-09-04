from datetime import datetime

from flask import Flask, redirect, render_template_string, request

app = Flask(__name__)
study_logs = []

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
  <p>컨테이너 안에서 실행 중인 작은 웹앱입니다.</p>

  <form method="post">
    <label for="title">오늘 배운 주제</label>
    <input id="title" name="title" placeholder="예: Docker 포트 연결" required>

    <label for="content">학습 내용</label>
    <textarea id="content" name="content" rows="4"
      placeholder="오늘 이해한 내용을 적어 보세요." required></textarea>

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

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        study_logs.insert(
            0,
            {
                "title": request.form["title"],
                "content": request.form["content"],
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            },
        )
        return redirect("/")

    return render_template_string(PAGE, study_logs=study_logs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)