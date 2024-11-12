import pandas as pd

file = 'C:/Users/Anca/Documents/GitHub/EvolveGCN/data/Processed_Refugee_Stock_Data_Edges.xlsx'
# Load the Excel file (adjust the file path as needed)
data = pd.read_excel(file)
# Replace the first column with line numbers (1-based indexing)
data = data[data.iloc[:, 2] >= 2]
 # Save the modified DataFrame to a new Excel file
data.to_excel(file, index=False)
