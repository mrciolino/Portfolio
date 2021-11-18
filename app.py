from flask import Flask, request, render_template, jsonify, send_file
import subprocess
import sys
import os

sys.path.append(os.getcwd() + "/projects/iris_classifier")
sys.path.append(os.getcwd() + "/static/contact")
from contact import send_simple_message
from predict_iris import run_iris

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    for website in ["https://deepfakeservice.herokuapp.com",
                    "https://sea-of-thieves-cooking-app.herokuapp.com/",
                    "https://aidndgen.herokuapp.com/",
                    "https://share.streamlit.io/mrciolino/crowd-counter/main/main.py",
                    "https://share.streamlit.io/mrciolino/yolov3_deepsort/main.py"]:
        subprocess.Popen(['curl ' + website],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         shell=True)
    return render_template('index.html')


@app.route('/test_project')
def test_project():
    return render_template('iris.html')


@app.route('/spie_presentation')
def spie_presentation():
    return send_file("static/refs/Super Resolution SPIE.pdf",
                     'application/pdf',
                     as_attachment=False,
                     attachment_filename="Ciolino SPIE Presentation.pdf")


@app.route('/go_ppt')
def go_ppt():
    return send_file("static/refs/GoPaperPPTai4i.pdf",
                     'application/pdf',
                     as_attachment=False,
                     attachment_filename="GoPaperPPTai4i.pdf")


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
    app.run(host='0.0.0.0', port=port, debug=False)
