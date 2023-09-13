import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")
# Convert height from cm to m
# Calculate BMI
# Add 'overweight' column
df["overweight"] = (df["weight"] / ((df["height"]/100) ** 2)).apply(lambda x: 1 if x >= 25 else 0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df["cholesterol"] = df["cholesterol"].apply(lambda x: 1 if x > 1 else 0)
df["gluc"] = df["gluc"].apply(lambda x: 1 if x > 1 else 0)

df = df[(df['ap_lo'] <= df['ap_hi']) 
    & (df['height'] >= df['height'].quantile(0.025)) 
    & (df['height'] <= df['height'].quantile(0.975)) 
    & (df['weight'] >= df['weight'].quantile(0.025)) 
    & (df['weight'] <= df['weight'].quantile(0.975))]

def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_melt = pd.melt(
        df,
        value_vars=["active", "alco", "cholesterol", "gluc", "overweight", "smoke"],
        id_vars=["cardio"],
    )

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_melt["total"] = 1
    df_cat = df_melt.groupby(["cardio", "variable", "value"], as_index=False).count()

    # Draw the catplot with 'sns.catplot()'
    g = sns.catplot(
        x="variable",
        y="total",
        data=df_cat,
        hue="value",
        col="cardio",
        kind="bar"
    )
    g.set_axis_labels("variable", "total")
    fig = g.fig

    # Do not modify the next two lines
    fig.savefig("catplot.png")
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    # height is less than the 2.5th percentile 
    # (Keep the correct data with (df['height'] >= df['height'].quantile(0.025)))
    # height is more than the 97.5th percentile
    # weight is less than the 2.5th percentile
    # weight is more than the 97.5th percentile

    # Calculate the correlation matrix
    corr = df.corr()
    
    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(11, 9))
    
    # Draw the heatmap with 'sns.heatmap()'
    df_heat = sns.heatmap(corr, annot=True, fmt=".1f", mask=mask, cmap='coolwarm', vmax=.3, center=0, square=True, linewidths=.5, cbar_kws={"shrink": .5})

  
    # Do not modify the next two lines
    fig.savefig("heatmap.png")
    return fig