import pickle
import pandas as pd
import streamlit as st

COLUMNS = [
    "age",
    "sex",
    "cp",
    "trestbps",
    "chol",
    "fbs",
    "restecg",
    "thalach",
    "exang",
    "oldpeak",
    "slope",
    "ca",
    "thal",
    "target",
]
FEATURES = ["age", "sex", "cp", "chol", "ca"]

# load the trained model. this will be an sklearn DecisionTreeClassifier
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# read the full dataset, so we can visualize the distribution of the features
df = pd.read_csv("heart_disease.csv", names=COLUMNS, na_values="?").dropna()

# display some text
st.title("Heart Disease Risk Predictor")

# ask the user to input values for the features used by the model
age = st.number_input("Age", min_value=1, max_value=120, value=50)
sex = st.selectbox(
    "Sex", options=[("Male", 1), ("Female", 0)], format_func=lambda x: x[0]
)[1]
cp = st.selectbox(
    "Chest Pain Type",
    options=[
        (1, "Typical angina"),
        (2, "Atypical angina"),
        (3, "Non-anginal pain"),
        (4, "Asymptomatic"),
    ],
    format_func=lambda x: x[1],
)[0]
chol = st.number_input(
    "Serum Cholesterol (mg/dl)", min_value=100, max_value=600, value=200
)
ca = st.selectbox("Number of Major Vessels (0–3)", options=[0, 1, 2, 3])

# if the user clicks the "Predict" button, use the model to make a prediction and
# display the result
if st.button("Predict"):
    prediction = model.predict([[age, sex, cp, chol, ca]])[0]
    if prediction == 1:
        st.error("High risk of heart disease.")
    else:
        st.success("Low risk of heart disease.")

# display a bar chart showing the distribution of outcomes for similar patients in the
# dataset (same sex and similar age)
st.subheader("Outcomes for Similar Patients")
similar = df[(df["sex"] == sex) & (df["age"].between(age - 10, age + 10))]
counts = pd.Series({
    "Low Risk": (similar["target"] == 0).sum(),
    "High Risk": (similar["target"] > 0).sum(),
})
st.bar_chart(counts)
