import pandas as pd
df = pd.read_csv("https://data.seattle.gov/api/views/tw7j-dfaw/rows.csv")

def test_create_dataframe(df, columnName):
    for col in df.columns:  # first condition
        if col not in columnName:
            return false
    for b in df.dtypes:
        if b != object:
            return false
    if df.shape[1] < 10:  # third one
        return false
    return true
