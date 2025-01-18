import zipfile
import pandas as pd

# Path to your ZIP file
zip_path = 'data/SPY_1min_sample_firstratedata.zip'

# Open the ZIP file
with zipfile.ZipFile(zip_path, 'r') as z:
    # List all files in the ZIP archive
    file_list = z.namelist()
    print("Files in ZIP archive:", file_list)
    
    # Assuming the file of interest is the first one in the ZIP archive
    target_file = file_list[0]  # Adjust index if needed
    
    # Open the target file as a pandas DataFrame
    with z.open(target_file) as f:
        df = pd.read_csv(f)
        # Display the first few lines of the DataFrame
        print(df.head())