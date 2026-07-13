from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><title>Kube Demo</title></head>
<body style="font-family:sans-serif;text-align:center;margin-top:80px">
  <h1>Kube Demo</h1>
  <p>Application Flask dockerisee avec succes.</p>
  <p>Auteur : Jason</p>
</body></html>"""

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
