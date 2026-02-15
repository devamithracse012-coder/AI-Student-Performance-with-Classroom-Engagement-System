import azure.functions as func
import json
import joblib
import os

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

# Load trained model
model = joblib.load(os.path.join(os.getcwd(), "model.pkl"))

@app.route(route="predict", auth_level=func.AuthLevel.ANONYMOUS)
def predict(req: func.HttpRequest) -> func.HttpResponse:
    try:
        data = req.get_json()

        study_hours = float(data.get("study_hours", 0))
        attendance = float(data.get("attendance", 0))

        # Simple working logic (STABLE VERSION)
        score = (study_hours * 5) + (attendance * 0.5)

        if score >= 75:
            result = "Excellent"
        elif score >= 50:
            result = "Average"
        else:
            result = "Needs Improvement"

        response = {
            "predicted_score": round(score, 2),
            "performance": result
        }

        return func.HttpResponse(
            json.dumps(response),
            mimetype="application/json",
            headers={
                "Access-Control-Allow-Origin": "*"
            }
        )

    except Exception as e:
        return func.HttpResponse(str(e), status_code=400)
