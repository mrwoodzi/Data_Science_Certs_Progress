# Import required libraries
import pandas as pd
import dash
from dash import html 
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df["Payload Mass (kg)"].max()
min_payload = spacex_df["Payload Mass (kg)"].min()

# Create a dash application
app = dash.Dash(__name__)

# https://dash.plotly.com/layout
# https://dash.plotly.com/dash-html-components
# Create an app layout
try:
    app.layout = html.Div(
        children=[
            html.H1(
                "SpaceX Launch Records Dashboard",
                style={
                    "textAlign": "center", 
                    "color": "#006400", 
                    "font-size": 40},
                    ),
            # TASK 1: Add a dropdown list to enable Launch Site selection
            # The default select value is for ALL sites
            dcc.Dropdown(id='site-dropdown',
                        options=[
                            {'label': 'All Sites', 'value': 'ALL'},
                            {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'}, 
                            {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
                            {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                            {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'},
                            ],
                            value='ALL',
                            placeholder=" ",
                            searchable=True,
                        ),
            # TASK 2: Add a pie chart to show the total successful launches count for all sites
            # If a specific launch site was selected, show the Success vs. Failed counts for the site
            # https://dash.plotly.com/dash-html-components/div
            html.Div(
                dcc.Graph(
                    id=" site-success-pie-chart")
                    ),
            html.Br(),
            # https://dash.plotly.com/dash-html-components/p
            html.P("Payload range (Kg):"),
            # TASK 3: Add a slider to select payload range
            # dcc.RangeSlider(id='payload-slider',...)
            # TASK 4: Add a scatter chart to show the correlation between payload and launch success
            html.Div(
                dcc.Graph(
                    id="success-payload-scatter-chart")
                    ),
        ])
except:
    app.layout = html.Div(
        children=[
            html.H1(
                ("You Suck!\n Don't be Stupid!\n FIX IT!"),
                style={
                    "textAlign": "center",
                    "color": "#FF0000",
                    "font-size": 40},
                    ),
        ])
# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
@app.callback(
        Output("site-success-pie-chart", "figure"),
        Input("site-dropdown", "value")
        )
def launch_site_success_pie_chart(entered_site):
    filtered_df = spacex_df.loc[spacex_df["Launch Site"] == entered_site]
    if entered_site == "ALL":
        fig = px.pie(filtered_df, values="class", names="Launch Site", title="Total Success Launches by Site")
        pass
    else:
        pass
# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
# try:
#     @app.callback(
#             Output("payload-slider", "figure"),
#             Input("site-dropdown", "value")
#             )
# except: 
#     pass
# @callback(
#     Output("click-output", "children"),
#     Input("click-div", "n_clicks")
#     )
# def click_counter(n_clicks):
#     return f"The html.Div above has been clicked this many times: {n_clicks}"
# Run the app
if __name__ == "__main__":
    app.run_server(debug=True) # debug=True # enables hot reloading so as changes are made, changes are seen
