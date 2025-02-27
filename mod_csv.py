import pandas as pd
from dash import Dash

df_list = []
for i in range(3):
    name = "data\daily_sales_data_"
    df = pd.read_csv(name + str(i) + ".csv")
    print(df.head())
    df = df[df["product"] == "pink morsel"]
    print(type(df["quantity"][0]))
    df["price"] = (df["price"].str[1:]).astype(float)
    df["sales"] = df["price"] * df["quantity"]
    df = df[["sales", "date", "region"]]

    df_list.append(df)
df_main = pd.concat(df_list, ignore_index=True)
df_main.to_csv("combined_tidy_csv.csv", index =False)
