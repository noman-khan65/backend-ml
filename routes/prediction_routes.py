from flask import Blueprint, request, jsonify

from services.prediction_service import PredictionService
from schemas.prediction_schema import validate_prediction_request


prediction_bp = Blueprint(
    "prediction",
    __name__
)


service = PredictionService()



@prediction_bp.route(
    "/predict",
    methods=["POST"]
)
def predict():


    try:

        data = request.get_json()


        validate_prediction_request(
            data
        )


        result = service.predict_sales(
            data["month"]
        )


        return jsonify(result),200



    except Exception as e:


        return jsonify({

            "error":str(e)

        }),400