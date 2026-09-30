"""Train a logistic regression model on cleaned survey data."""

import json
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


def train(data_path, output_dir, config):
    df = pd.read_csv(data_path)
    X = df.drop(columns=["participant_id", "outcome"])
    y = df["outcome"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=config["test_size"], random_state=config["seed"]
    )

    model = LogisticRegression(C=config["regularization"])
    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)
    print(f"Test accuracy: {accuracy:.3f}")

    predictions = model.predict(X_test)
    pd.DataFrame({"prediction": predictions}).to_csv(
        f"{output_dir}/predictions.csv", index=False
    )

    with open(f"{output_dir}/metrics.json", "w") as f:
        json.dump({"accuracy": accuracy, "n_train": len(X_train)}, f)


if __name__ == "__main__":
    with open("config.json") as f:
        config = json.load(f)
    train("data/cleaned/merged.csv", "results/model_v1", config)
