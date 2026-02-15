import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

# Create sample dataset
data = {
    "study_hours": [1,2,3,4,5,6,7,8,9,10],
    "attendance": [50,55,60,65,70,75,80,85,90,95],
    "score": [35,40,50,55,60,70,75,85,90,95]
}

df = pd.DataFrame(data)

X = df[["study_hours", "attendance"]]
y = df["score"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")

print("Model trained and saved successfully!")
