from flask import request, jsonify
from my_app import app

tweets = {}

@app.route("/")
def home():
    return "Flask 정상 작동!"

@app.route("/tweet", methods=["POST"])
def create_tweet():
    data = request.get_json()

    tweet_id = data["id"]
    tweet_text = data["tweet"]

    tweets[tweet_id] = tweet_text

    return jsonify({
        "status": "success",
        "id": tweet_id,
        "tweet": tweet_text
    })
