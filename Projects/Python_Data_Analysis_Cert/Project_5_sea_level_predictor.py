import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from CSV file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Sea Level')

    # Get x and y values
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    # Perform linear regression for all data
    slope, intercept, r_value, p_value, std_err = linregress(x, y)

    # Plot the first line of best fit
    x1 = list(range(1880, 2051))
    y1 = [intercept + slope * year for year in x1]
    plt.plot(x1, y1, 'r', label='Best Fit Line 1')

    # Perform linear regression for data since year 2000
    x_future = df[df['Year'] >= 2000]['Year']
    y_future = df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level']
    new_fit = linregress(x_future, y_future)
    new_slope = new_fit.slope
    new_intercept = new_fit.intercept

    # Plot the second line of best fit
    x_future2 = list(range(2000, 2051))
    y_future2 = [new_intercept + new_slope * year for year in x_future2]
    plt.plot(x_future2, y_future2, 'r', label='Best Fit Line 2', color='green')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Add legend
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()