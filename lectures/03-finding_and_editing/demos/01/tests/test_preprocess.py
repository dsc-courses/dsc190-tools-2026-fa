"""Tests for preprocessing functions."""

from src.preprocess import load_participants, load_responses


def test_load_participants_clips_age():
    df = load_participants("data/raw/participants.csv")
    assert df["age"].min() >= 18
    assert df["age"].max() <= 99


def test_load_responses_cleans_columns():
    df = load_responses("data/raw/survey_responses.csv")
    assert all("_" in col or col.islower() for col in df.columns)
