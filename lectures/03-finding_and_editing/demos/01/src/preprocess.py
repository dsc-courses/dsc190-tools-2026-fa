"""Preprocess raw survey data for modeling."""

import pandas as pd


def load_participants(path):
    df = pd.read_csv(path)
    df["age"] = df["age"].clip(lower=18, upper=99)
    df["zip_code"] = df["zip_code"].astype(str).str.zfill(5)
    return df


def load_responses(path):
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    return df


def merge_data(participants, responses):
    return participants.merge(responses, on="participant_id", how="inner")


if __name__ == "__main__":
    participants = load_participants("data/raw/participants.csv")
    responses = load_responses("data/raw/survey_responses.csv")
    merged = merge_data(participants, responses)
    merged.to_csv("data/cleaned/merged.csv", index=False)
    print(f"Saved {len(merged)} records.")
