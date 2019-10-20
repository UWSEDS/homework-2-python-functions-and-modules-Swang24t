import pandas as pd
df = pd.read_csv("https://data.seattle.gov/api/views/tw7j-dfaw/rows.csv")

def test_create_dataframe(df, columnName):
    for col in df.columns:  # first condition check if in list 
        if col not in columnName:
            return false
    for b in df.dtypes:#determine if same 
        if b == object:
            return false
    if df.shape[1] < 10:  # third one determine the size
        return false
    return true
