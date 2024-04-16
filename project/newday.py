import os
from main3 import start
files = [
    "india.csv",
    "world.csv",
     "tech.csv",
    "business.csv",
    "sports.csv"
         ]

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

start()