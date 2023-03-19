import pandas as pd

SHEET_ID = '1-QFHeOYXZt6_wL3UElMnUgiGs9ccmKeE3rBGpfA9ru0'
SHEET_NAME = 'AAPL'
url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
df = pd.read_csv(url)
print(df.head())
