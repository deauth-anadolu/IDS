

import joblib
import pathlib

DIR = pathlib.Path(__file__).parent.resolve()

class Detector:
    model = None

    def __init__(self, filename) -> None:
        self.filename = filename
        Detector.load_model(filename)

    @classmethod
    def load_model(cls, filename):
        cls.model = joblib.load(f"{DIR}/ml_model/models/{filename}")

    @staticmethod
    def predict_attack(data):
        pred = Detector.model.predict(data) # type: ignore
        return pred