from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd

app = Dash()

colors = {
    'background': '#1E1E1E',
    'card': '#2C2C2C',
    'text': '#F4A261',
    'graph_bg': '#333333',
    'accent': '#E76F51'
}

df = pd.read_csv("combined_tidy_csv.csv")
df["date"] = pd.to_datetime(df["date"]).dt.date

fig = px.line(df, x="date", y="sales", title="Pink-Morsels Sales Over Time",
              labels={"date": "Date", "sales": "Sales (Dollars)"},
              template="plotly_dark")
fig.update_traces(line=dict(width=2.5, color=colors['accent']))
fig.update_layout(
    title_x=0.5,
    plot_bgcolor=colors['graph_bg'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
    margin=dict(l=40, r=40, t=50, b=50),
)

app.layout = html.Div(style={'backgroundColor': colors['background'], 'padding': '20px'}, children=[
    html.H1("Pink-Morsels Sales Dashboard", 
            style={'textAlign': 'center', 'color': colors['text'], 'marginBottom': '20px'}),
    
    html.Div(style={'backgroundColor': colors['card'], 'padding': '15px', 'borderRadius': '10px'}, children=[
        dcc.Graph(id="pink-morsel-sales-over-time", figure=fig),
        
        html.Br(),
        
        html.Label("Select Region:", style={'color': colors['text'], 'fontSize': '18px'}),
        dcc.RadioItems(
            id='reg_button', 
            options=[{'label': region.capitalize(), 'value': region} for region in ["all", "north", "east", "south", "west"]],
            value="all", 
            inline=True,
            style={'color': colors['text'], 'margin': '10px 0'}
        )
    ])
])

@callback(
    Output("pink-morsel-sales-over-time", "figure"),
    Input("reg_button", "value")
)
def update_output_div(input_value):
    if input_value == 'all':  
        dff = df
    else:
        dff = df[df['region'] == input_value]
    
    fig = px.line(dff, x="date", y="sales", title="Pink-Morsels Sales Over Time",
                  labels={"date": "Date", "sales": "Sales (Dollars)"},
                  template="plotly_dark")
    
    fig.update_traces(line=dict(width=2.5, color=colors['accent']))
    fig.update_layout(
        title_x=0.5,
        plot_bgcolor=colors['graph_bg'],
        paper_bgcolor=colors['background'],
        font_color=colors['text'],
        margin=dict(l=40, r=40, t=50, b=50),
    )
    
    return fig

if __name__ == '__main__':
    app.run(debug=True)

