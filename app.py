
from flask import Flask, render_template, request, redirect, url_for,jsonify
from flask_cors import CORS
from predict_types import predict_type,recreate_model, predict_tweet
from twitterscraper import tweet_return

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['GET', 'POST'])
def testfn():
    # GET request
    if request.method == 'GET':
        message = {'greeting':'Hello from Flask!'}
        return jsonify(message)  # serialize and use JSON headers
    # POST request
    if request.method == 'POST':
        data = request.get_json()  # parse as JSON
        user_text = data["data"]
        user_type = predict_type(user_text)
        return jsonify({"type":str(user_type)}),200

@app.route('/tweet_pred', methods=['GET', 'POST'])
def tweet():
    # GET request
    if request.method == 'GET':
        message = {'greeting':'Hello from Flask!'}
        return jsonify(message)  # serialize and use JSON headers
    # POST request
    if request.method == 'POST':
        data = request.get_json()  # parse as JSON
        user_handle = data["handle"]
        tweet_return(user_handle)
        user_type = predict_tweet(user_handle)
        return jsonify({"type":str(user_type)}),200

if __name__ == '__main__' :
    app.run(debug=True,port=5000)