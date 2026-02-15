import json
import joblib
import numpy as np
import os

def init():
    global model
    model_path = os.path.join(os.getenv("AZUREML_MODEL_DIR"), "data.learner")
    model = joblib.load(model_path)

def run(raw_data):
    try:
        data = json.loads(raw_data)
        study_hours = data["study_hours"]
        attendance = data["attendance"]

        input_data = np.array([[study_hours, attendance]])
        prediction = model.predict(input_data)

        return {"prediction": prediction.tolist()}
    except Exception as e:
        return {"error": str(e)}