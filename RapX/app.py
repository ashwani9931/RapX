from flask import Flask, jsonify, render_template, request

app = Flask(__name__)  # static_folder="static", template_folder="templates" by default


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.post("/api/book")
def book():
    payload = request.get_json(silent=True) or {}
    if not isinstance(payload, dict):
        payload = {}
    name = str(payload.get("name", "")).strip()
    message = f"Thanks{', ' + name if name else ''}! Your class request has been received."
    return jsonify(message=message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8009, debug=True)
