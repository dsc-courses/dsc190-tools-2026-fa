# Data Dictionary

## participants.csv

| Column         | Type   | Description                     |
|----------------|--------|---------------------------------|
| participant_id | int    | Unique identifier               |
| name           | string | Participant first name          |
| age            | int    | Age in years                    |
| zip_code       | string | 5-digit US zip code             |
| state          | string | 2-letter state abbreviation     |

## survey_responses.csv

| Column         | Type   | Description                     |
|----------------|--------|---------------------------------|
| participant_id | int    | Links to participants table     |
| Question 1-4   | int    | Likert scale response (1-5)     |
| outcome        | int    | Binary outcome (0 or 1)         |
