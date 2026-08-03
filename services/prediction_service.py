import pandas as pd

from repositories.model_repository import ModelRepository
from utils.stage_classifier import classify_stage



class PredictionService:


    def __init__(self):

        self.repository = ModelRepository()


    def predict_sales(self, month):

        model = self.repository.load_model()


        input_data = pd.DataFrame({

            "month":[month]

        })


        prediction = model.predict(
            input_data
        )[0]


        stage = classify_stage(month)


        return {

            "month": month,

            "predicted_sales": round(
                prediction
            ),

            "stage": stage

        }