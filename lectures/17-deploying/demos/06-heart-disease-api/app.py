import pickle

from fastapi import FastAPI

# load the trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

@app.get("/predict")
def predict(age: float, sex: int, cp: int, chol: float, ca: int):
    # the model expects the features in this exact order
    features = [[age, sex, cp, chol, ca]]
    prediction = int(model.predict(features)[0])
    return {
        "prediction": prediction,
        "risk": "high" if prediction == 1 else "low",
    }
