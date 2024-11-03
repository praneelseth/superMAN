import pandas as pd
import os

# Assuming the function get_man_page is defined as in the previous response
def get_man_page(command):
    try:
        # Using os.popen to get the output of the man command
        with os.popen(f'man {command}') as man_page:
            output = man_page.read()
        return output if output else f"No manual entry for {command}"
    except Exception as e:
        return f"Error retrieving man page for {command}: {e}"

# Read commands from the text file
with open("commands.txt", "r") as file:
    commands = [line.strip() for line in file if line.strip()]

# Generate the data for the DataFrame
data = []
for command in commands:
    man_page = get_man_page(command)
    data.append({"Command": command, "Man Page": man_page})

# Create DataFrame and save to CSV
df = pd.DataFrame(data)
df.to_csv("commands_with_man_pages.csv", index=False)
print("CSV file generated: commands_with_man_pages.csv")
