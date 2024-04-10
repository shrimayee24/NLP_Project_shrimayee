import os

files = ["C:\\Users\\AKANKSHA KALE\\Desktop\\NLP_Project\\project\\india.csv"]

for filepath in files:
    # Check if the file exists
    if os.path.exists(filepath):
        # Open the file in binary write mode
        with open(filepath, "wb") as f:
            # Truncate the file
            f.truncate()
        print(f"File '{filepath}' truncated successfully.")
    else:
        print(f"File '{filepath}' does not exist.")
