import pandas as pd

df = pd.read_json("dataset_sales_pandas.json")

df.to_csv("dataset_sales_pandas.csv")