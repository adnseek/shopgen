import pandas as pd
import json

# Read CSV file with ";" as separator
df = pd.read_csv('awin_14_12_2022.csv', sep=';')

# Convert each row to a dictionary and then to a JSON string
json_array = [json.dumps(row.to_dict()) for _, row in df.iterrows()]

# Write the list of strings to a file
with open('awin.json', 'w') as f:
    f.write(json.dumps(json_array))
