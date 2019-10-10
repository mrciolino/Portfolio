from flask import Flask, request, render_template, jsonify
import sys
import os

sys.path.append(os.getcwd() + "/projects/iris_classifier")
from predict_iris import run_iris
sys.path.append(os.getcwd() + "/projects/job_tag_classifier")
import predict_job_tag
sys.path.append(os.getcwd() + "/projects/politican_classifier")
from predict_politican import predict_vote
sys.path.append(os.getcwd() + "/static/contact")
from contact import send_simple_message

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test_project')
def test_project():
    return render_template('iris.html')


@app.route('/job_tag_classifier')
def job_tag_classifier():
    return render_template('jobtag.html')


@app.route('/politician_classifier')
def politician_classifier():
    return render_template('politicians.html')


@app.route('/predict_iris', methods=['POST'])
def predict_iris():

    app.logger.info('Running Iris Classifers')
    # get the data
    data = request.get_json()
    # convert data into array
    features = [float(i) for i in list(data[0].values())]
    app.logger.info(features)
    # run the prediction and return
    result = run_iris(features)
    app.logger.info(result)
    return jsonify(result=result)


@app.route('/job_tag_classifier', methods=['POST'])
def predict_tags():

    app.logger.info('Running Job Tag Classifer')
    # get the data
    data = request.get_json()
    # convert data into array
    features = [i for i in list(data[0].values())]
    app.logger.info("Title: %s" % features[0])
    # run the prediction and return
    result = predict_job_tag.run_predictions(features)
    app.logger.info(result)
    return jsonify(result=result)


@app.route('/poltician_predict', methods=['POST'])
def predict_votes():

    app.logger.info('Running Voting Classifer')
    # get the data
    data = request.get_json()
    # convert data into array
    features = [i for i in list(data[0].values())]
    app.logger.info("Poltician: %s Description: %s" % (features[1], features[0]))
    # run the prediction and return
    result = predict_vote(features)
    app.logger.info(result[0])
    return jsonify(result=result)


@app.route('/post_mail', methods=['POST'])
def post_mail():

    app.logger.info('Sending mail to server')
    # get the data
    data = request.get_json()
    # convert data into array
    features = [i for i in list(data[0].values())]
    # send the mail to mailgun server
    result = send_simple_message(*features)
    app.logger.info("Email Results:", result)
    return jsonify(result=result)


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
