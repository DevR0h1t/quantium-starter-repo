# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()
df = pd.read_csv("combined_tidy_csv.csv")
df["date"] = pd.to_datetime(df["date"]).dt.date
fig = px.line(df, x="date", y="sales", title="sales over time", labels={"date":"date", "sales": "sales(dollars)"})
fig.update_layout(title_x=0.5)
app.layout = html.Div(children=[
    html.H1("Pink-Morsels sales over time"),
    dcc.Graph(id="pink-morsel-sales/time", figure=fig)      
                                ])
if __name__ == '__main__':
    app.run(debug=True)
