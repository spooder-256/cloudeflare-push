from pathlib import Path

from flask import Flask, Response

app = Flask(__name__)

# Read the page once; it is served as-is (no templating).
PAGE = (Path(__file__).parent / "templates" / "index.html").read_text(encoding="utf-8")


@app.route("/")
def home():
    return Response(PAGE, mimetype="text/html")


if __name__ == "__main__":
    app.run(debug=True)