from flask import Flask, jsonify, request
from classifier import get_prediction

app = Flask.app(__name__)
@app.route("/predict-digit", methods=["POST"])

def predict_data():
    Image = request.files.get("digit")
    prediction = get_prediction(image)
    return jsonify({
        "prediction":prediction
    },200)

if __name__ == "__main__":
    app.run(debug=True)