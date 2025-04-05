from flask import Flask, request, jsonify
from flask_cors import CORS
from main import recommend_movie, GENRES, PLATFORMS

app = Flask(__name__)
CORS(app)

@app.route("/api/recommend", methods=["POST"])
def recommend():
    data = request.json
    genre = data.get("genre", "").lower()
    platform = data.get("platform", "").lower()

    if genre not in GENRES:
        return jsonify({"error": f"Unsupported genre: {genre}"}), 400
    if platform not in PLATFORMS:
        return jsonify({"error": f"Unsupported platform: {platform}"}), 400

    recommendation = recommend_movie(genre, platform)
    return jsonify({"recommendation": recommendation})

if __name__ == "__main__":
    app.run(debug=True)
