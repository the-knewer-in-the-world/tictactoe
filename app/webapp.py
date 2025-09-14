# app/webapp.py
from flask import Flask, jsonify, request
from app.game import TicTacToe

app = Flask(__name__)
game = TicTacToe()

@app.route('/')
def index():
    return jsonify({"msg":"TicTacToe API - use /state and /move"})

@app.route('/state')
def state():
    return jsonify(game.state())

@app.route('/move', methods=['POST'])
def move():
    data = request.json or {}
    pos = data.get("pos")
    if pos is None:
        return jsonify({"error":"send JSON {\"pos\":0..8}"}), 400
    try:
        game.make_move(int(pos))
        return jsonify(game.state())
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
