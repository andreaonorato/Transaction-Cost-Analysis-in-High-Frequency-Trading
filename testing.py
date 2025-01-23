import pandas as pd

# Load the Excel file
file_path = "data/Decentralized/Gas_fees_ETH.csv"  # Replace with your actual file path
df = pd.read_csv(file_path, dtype={'Date(UTC)': str})

# Convert the 'Date(UTC)' column to datetime format
df['Date(UTC)'] = pd.to_datetime(df['Date(UTC)'])

# Define the date range for filtering
start_date = pd.to_datetime("2021-07-04")
end_date = pd.to_datetime("2021-07-19")

# Filter rows within the specified date range
filtered_df = df[(df['Date(UTC)'] >= start_date) & (df['Date(UTC)'] <= end_date)]

# Retain only the 'UnixTimeStamp' and 'Value (Wei)' columns
cleaned_df = filtered_df[['Date(UTC)', 'Value (Wei)']]

correct_dates = [
    "2021-07-04", "2021-07-05", "2021-07-06", "2021-07-07",
    "2021-07-08", "2021-07-09", "2021-07-10", "2021-07-11",
    "2021-07-12", "2021-07-13", "2021-07-14", "2021-07-15",
    "2021-07-16", "2021-07-17", "2021-07-18", "2021-07-19"
]

# Assign the corrected dates back to the 'Date(UTC)' column
cleaned_df['Date(UTC)'] = correct_dates

# Save the cleaned data to a new Excel file
output_file = "cleaned_Gas_fees_ETH.xlsx"
cleaned_df.to_excel(output_file, index=False)

print(f"Cleaned data has been saved to {output_file}")
