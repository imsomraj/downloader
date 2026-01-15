from flask import Flask, request, jsonify
from streamtape_dl import get_dl_link

app = Flask(__name__)

@app.route("/")
def home():
    return {"status": "Streamtape Downloader API is running"}

@app.route("/dl")
def dl():
    url = request.args.get("url")
    if not url:
        return jsonify({"error": "URL parameter is required"}), 400

    link = get_dl_link(url)
    if not link:
        return jsonify({"error": "Failed to fetch direct link"}), 500

    return jsonify({"direct_link": link})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
