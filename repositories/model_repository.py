import joblib
from pathlib import Path


class ModelRepository:

    def __init__(self):

        self.model_path = Path(
            "models/plc_polynomial_v1.pkl"
        )

        self.model = None


    def load_model(self):

        if self.model is None:

            self.model = joblib.load(
                self.model_path
            )

        return self.model