import datetime

# Get the current date
now = datetime.datetime.now()

# Open the input file
with open('file.txt', 'r') as file:
    # Read all lines in the file
    lines = file.readlines()
    
# Create a list to hold the modified lines
modified_lines = []

# Iterate through the lines
for line in lines:
    # Check if the line contains the tag "#ResultProc"
    if "#ResultProc" in line:
        # Remove the content before the tag and the tag itself
        modified_line = line.split("#ResultProc")[-1]
        # Append the modified line to the list
        modified_lines.append(modified_line)

# Create the name of the output file with the date
output_file = "relatorio_creditos_automaticos_{}.txt".format(now.strftime("%Y-%m-%d"))

# Write the modified lines to the output file
with open(output_file, 'w') as file:
    file.writelines(modified_lines)