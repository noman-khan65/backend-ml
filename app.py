from flask import Flask

from routes.prediction_routes import prediction_bp



app = Flask(__name__)


app.register_blueprint(
    prediction_bp
)



@app.route("/")
def home():

    return {
        "message":
        "PLC Prediction API Running"
    }



if __name__=="__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )