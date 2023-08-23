import pandas as pd

# Read the formatted_text.txt file
with open('formatted_text.txt', 'r') as file:
    lines = file.readlines()

# Create empty lists to store names, first numerical values, and second numerical values
names = []
numerical_values_1 = []
numerical_values_2 = []

# Iterate through lines to extract names and numerical values
for line in lines:
    line = line.strip()  # Remove leading/trailing whitespaces
    if line.startswith("CITY OF SAN ANTONIO - PROPOSITION A") or line.startswith("TOTAL VOTE %") or line.startswith("For Council, City of San Antonio, District") or line.startswith("Overvotes") or line.startswith("Undervotes"):
        # Skip these lines
        continue
    
    parts = line.rsplit(' ', 2)  # Split at the second to last space
    name = parts[0]
    value_1 = parts[1]
    value_2 = parts[2].replace('%', '')  # Remove the percentage sign
    names.append(name)
    numerical_values_1.append(value_1)
    numerical_values_2.append(value_2)

# Create a pandas DataFrame
data = {'Name': names, 'Numerical Value 1': numerical_values_1, 'Numerical Value 2': numerical_values_2}
df = pd.DataFrame(data)

# I'm dropping the useless first row of the df
df.drop(0, inplace=True)

#renaming the columns 
df.rename(columns={'Numerical Value 1': 'Votes', 'Numerical Value 2': 'Percentage of Vote'}, inplace=True)
df.rename(columns={'Name': 'Candidate'}, inplace=True)

# Convert 'Percentage of Vote' column to float with % sign
df['Percentage of Vote'] = df['Percentage of Vote'].str.rstrip('%').astype(float).map('{:.2f}%'.format)

# Convert 'Votes' column to int, replace names with 0
df['Votes'] = pd.to_numeric(df['Votes'], errors='coerce').fillna(0).astype(int)

#removing these rows
df.head(50)