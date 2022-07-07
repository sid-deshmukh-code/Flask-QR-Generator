from flask import Flask, render_template, request, send_file
from flask_qrcode import QRcode
import qrcode


app = Flask(__name__)
QRcode(app)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        text_ = request.form.get("fname")
        data = request.args.get("data", "")
        url_ = 
    return render_template("index.html")


@app.route("/qrcode", methods=["GET"])
def get_qrcode():
    # please get /qrcode?data=<qrcode_data>
    data = request.args.get("data", "")
    return send_file(qrcode(data, mode="raw"), mimetype="image/png")


if __name__ == '__main__':
    app.run(debug=True)
