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
# Create app.layout
app.layout = html.Div(
                    children=[
                            html.H1(
                                "SpaceX Launch Records Dashboard",
                                style={
                                    "textAlign": "center", 
                                    "color": "#006400", 
                                    "font-size": 40},
                                    ),
                            # Dropdown list to enable Launch Site selection
                            # The default select value is for ALL sites
                            dcc.Dropdown(
                                        id='site-dropdown',
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
                            # Add a pie chart to show the total successful launches count for all sites
                            # If a specific launch site was selected, show the Success vs. Failed counts for the site
                            # https://dash.plotly.com/dash-html-components/div
                            html.Div(
                                dcc.Graph(
                                    id="launch-site-success-pie-chart")
                                    ),
                            html.Br(),
                            # https://dash.plotly.com/dash-html-components/p
                            html.P("Payload range (Kg):"),
                            # Add a slider to select payload range
                            dcc.RangeSlider(id='payload-slider',
                                            min=0, 
                                            max=10000, 
                                            step=1000,
                                            marks={0: '0', 2500: '2500', 5000: '5000', 7500: '7500', 10000: '10000'},
                                            value=[min_payload, max_payload]
                                            ),
                            # Add a scatter chart to show the correlation between payload and launch success
                            html.Div(
                                dcc.Graph(
                                    id="success-payload-scatter-chart")
                                    ),
                        ])
    

# Add a callback function for `site-dropdown` as input, launch-site-success-pie-chart` as output
@app.callback(
        Output("launch-site-success-pie-chart", "figure"), # uses def launch_site_success_pie_chart(entered_site)
        Input("site-dropdown", "value")
        )
def launch_site_success_pie_chart(entered_site):
    filtered_df = spacex_df.loc[spacex_df["Launch Site"] == entered_site]
    if entered_site == "ALL":
        fig = px.pie(spacex_df, 
                     values="class", 
                     names="Launch Site", 
                     title="Total Success Launches by Site")
    else:
        fig = px.pie(filtered_df, 
                     names="class", 
                     title="Total Success Launches for Site")
    return fig


# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(
        Output("success-payload-scatter-chart", "figure"),
        Input("site-dropdown", "value"), 
        Input("payload-slider", "value")
        )
def success_payload_scatter_chart(entered_site, payload_range):
   min_payload = payload_range[0]
   max_payload = payload_range[1]
   all_spacex_df = spacex_df.loc[
                            spacex_df['Payload Mass (kg)'].between(min_payload, max_payload)
                            ]
   filtered_df = spacex_df.loc[
                            (spacex_df["Launch Site"] == entered_site) 
                            & 
                            (spacex_df['Payload Mass (kg)'].between(min_payload, max_payload))
                            ]
   if entered_site == "ALL":
       fig = px.scatter(all_spacex_df, 
                        x="Payload Mass (kg)", 
                        y="class", 
                        color="Booster Version Category") 
   else:
       fig = px.scatter(filtered_df, 
                        x="Payload Mass (kg)", 
                        y="class", 
                        color="Booster Version Category")
   return fig 

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True) # debug=True # enables hot reloading so as changes are made, changes are seen


# 1. Which site has the largest successful launches?
# 2. Which site has the highest launch success rate?
# 3. Which payload range(s) has the highest launch success rate?
# 4. Which payload range(s) has the lowest launch success rate?
# 5. Which F9 Booster version (v1.0, v1.1, FT, B4, B5, etc.) has the highest launch success rate?