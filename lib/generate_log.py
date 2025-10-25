from datetime import datetime
import os

def generate_log(data):
    #Validate input
    if not isinstance(data, list):
        raise ValueError("Input data must be a list.")

    #Generate a filename with today’s date
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    #Write the log entries to a file
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    #Print a confirmation message
    print(f"Log written to {filename}")

    # Return filename for testing
    return filename