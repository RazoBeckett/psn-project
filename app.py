import numpy as np
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from scipy.stats import norm

app = Flask(__name__)

@app.route("/normal-distribution", methods=["POST"])
@cross_origin()
def normal_distribution():
    data = request.json
    mean = float(data.get("mean", 0))
    std = float(data.get("std", 1))

    # Generate x values (e.g., range within 4 standard deviations)
    x = np.linspace(mean - 4 * std, mean + 4 * std, 100)
    # Calculate PDF values
    y = norm.pdf(x, mean, std)

    # Return x and y as JSON
    return jsonify({"x": x.tolist(), "y": y.tolist()})


if __name__ == "__main__":
    app.run(debug=True)
