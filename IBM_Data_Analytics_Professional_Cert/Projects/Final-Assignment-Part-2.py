# Dataset for XYZAutomotive 
# The dataset includes the following variables

# Date: The date of the observation.
# Recession: A binary variable indicating recession period; 1 means it was recession, 0 means it was normal.
# Automobile_Sales: The number of vehicles sold during the period.
# GDP: The per capita GDP value in USD.
# Unemployment_Rate: The monthly unemployment rate.
# Consumer_Confidence: A synthetic index representing consumer confidence, which can impact consumer spending and automobile purchases.
# Seasonality_Weight: The weight representing the seasonality effect on automobile sales during the period.
# Price: The average vehicle price during the period.
# Advertising_Expenditure: The advertising expenditure of the company.
# Vehicle_Type: The type of vehicles sold; Supperminicar, Smallfamiliycar, Mediumfamilycar, Executivecar, Sports.
# Competition: The measure of competition in the market, such as the number of competitors or market share of major manufacturers.
# Month: Month of the observation extracted from Date.
# Year: Year of the observation extracted from Date.

# Requirements to create the expected Dashboard
# Two dropdown menus: For choosing report type and year
# Each dropdown will be designed in a division


# The second dropdown (for selecting the year) should be enabled only if when the user selects “Yearly Statistics report” from the previous dropdown, else it should be disabled only. - The second dropdown (for selecting the year) should be enabled only if when the user selects “Yearly Statistics report” from the previous dropdown, else it should be disabled only.


# Layout for adding graphs.
# Callback functions to return to the layout and display graphs.
# First callback will be required to take the input for the report type and set the years dropdown to be enabled to take the year input for “Years Statistics Report”, else this dropdown be put on disabled.
# In the second callback you will fetch the value of report type and year and return the required graphs appropriately for each type of report
# The four plots to be displayed in 2 rows, 2 column representation

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

# Load the data using pandas
data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv')

# Initialize the Dash app
app = dash.Dash(__name__)

# Create the dropdown menu options
dropdown_options = [
    {'label': 'Yearly Statistics', 'value': 'Yearly Statistics'},
    {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}
]
# List of years 
year_list = [i for i in range(1980, 2024, 1)]

#---------------------------------------------------------------------------------------
# Create the layout of the app
app.layout = html.Div([
    #TASK 2.1 Add title to the dashboard
    html.H1("Automobile Sales Statistics Dashboard", 
            style={'textAlign': 'center', 
                   'color': '#503D36', 
                   'font-size': 24}),#May include style for title
    html.Div([#TASK 2.2: Add two dropdown menus
        html.Label("Select Statistics:"),
        dcc.Dropdown(
            id='dropdown-statistics',
            options=dropdown_options,
            value='Yearly Statistics',# change this to 'Yearly Statistics
            placeholder='Select a report type'
        )
    ]),
    html.Div(dcc.Dropdown(
            id='Select Year: ',
            options=[{'label': i, 'value': i} for i in year_list],
            value='1980' # setting a default val
        )),
    html.Div([#TASK 2.3: Add a division for output display
    html.Div(id='output-container', 
             className='chart-grid', 
             style={'display': 'flex'})])
])
#TASK 2.4: Creating Callbacks
# Define the callback function to update the input container based on the selected statistics
@app.callback(
    Output(component_id='select year', component_property='disabled'),
    Input(component_id='dropdown-statistics',component_property='disabled'))

def update_input_container(selected_statistics):
    if selected_statistics =='Yearly Statistics': 
        return False
    else: 
        return True

#Callback for plotting
# Define the callback function to update the input container based on the selected statistics
@app.callback(
    Output(component_id='output-container', component_property='children'),
    [Input(component_id='select-year', component_property='value'), 
     Input(component_id='dropdown-statistics', component_property='value')])


def update_output_container(selected_year, selected_statistics):
    if selected_statistics == 'Recession Period Statistics':
        # Filter the data for recession periods
        recession_data = data[data['Recession'] == 1]
        
#TASK 2.5: Create and display graphs for Recession Report Statistics

#Plot 1 Automobile sales fluctuate over Recession Period (year wise)
        # use groupby to create relevant data for plotting
        yearly_rec=recession_data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        R_chart1 = dcc.Graph(
            figure=px.line(yearly_rec, 
                x='Year',
                y='Automobile',
                title="Average Automobile Sales fluctuation over Recession Period"))

#Plot 2 Calculate the average number of vehicles sold by vehicle type, (only Recession Period - I put this in)
        # use groupby to create relevant data for plotting
        average_sales = recession_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()                           
        R_chart2  = dcc.Graph(
            figure=px.bar(average_sales, 
                           x='Vehicle_Type'
                           y='Automobile_Sales'
                           title='Average Number of Vehicles Sold by Type'))
        
# Plot 3 Pie chart for total expenditure share by vehicle type during recessions
        # use groupby to create relevant data for plotting
        exp_rec=  recession_data.groupby('Vehicle_Type')['Advertisement_Expenditure'].sum().reset_index()
        R_chart3 = dcc.Graph(
            figure=px.pie(exp_rec,
                          values='Advertisement_Expenditure',
                          names='Vehicle_Type',
                          title='Advertisement Expenditure Share by Vehicle Type during Recessions'))

# Plot 4 bar chart for the effect of unemployment rate on vehicle type and sales
        unemployment_effect = recession_data.groupby(['Unemployment_Rate', 'Vehicle_Type'])['Automobile_Sales'].mean().reset_index()
        R_chart4 = dcc.Graph(
            figure=px.bar(unemployment_effect,
                          x='Unemployment_Rate',
                          y='Automobile_Sales',
                          color='Vehicle_Type',
                          title='Effect of Unemployment Rate on Vehicle Type and Sales during Recessions'))

        return [
            html.Div(className='chart-item', children=[html.Div(children=R_chart1), html.Div(children=R_chart2)], style={...}),
            html.Div(className='chart-item', children=[html.Div(children=R_chart3), html.Div(children=R_chart4)], style={...})
            ]

# TASK 2.6: Create and display graphs for Yearly Report Statistics
 # Yearly Statistic Report Plots                             
    elif (input_year and selected_statistics=='Yearly Statistics') :
        yearly_data = data[data['Year'] == input_year]
                              
#TASK 2.5: Creating Graphs Yearly data
                              
#plot 1 Yearly Automobile sales using line chart for the whole period.
        yas= data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        Y_chart1 = dcc.Graph(figure=px.line(.................))
            
# Plot 2 Total Monthly Automobile sales using line chart.
        Y_chart2 = dcc.Graph(................)

            # Plot bar chart for average number of vehicles sold during the given year
        avr_vdata=yearly_data.groupby........................
        Y_chart3 = dcc.Graph( figure.................,title='Average Vehicles Sold by Vehicle Type in the year {}'.format(input_year)))

            # Total Advertisement Expenditure for each vehicle using pie chart
        exp_data=yearly_data.groupby(..................)
        Y_chart4 = dcc.Graph(...............)

#TASK 2.6: Returning the graphs for displaying Yearly data
        return [
                html.Div(className='.........', children=[html.Div(....),html.Div(....)],style={...}),
                html.Div(className='.........', children=[html.Div(....),html.Div(....)],style={...})
                ]
        
    else:
        return None

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)