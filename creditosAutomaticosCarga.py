import random

# Number of rows to generate in the output file
num_rows = 7000

# Open the input file for reading
with open("D.PAR.ETL.001.CRED.PERT.txt", "r") as input_file:
    # Read the contents of the file into a list of lines
    lines = input_file.readlines()

# Open the output file for writing
with open("D.PAR.ETL.001.CRED.PERT.CARGA.txt", "w") as output_file:
    # Repeat the process the desired number of times
    for i in range(num_rows):
        # Pick a random line from the input file
        line = random.choice(lines)
        # Split the line into fields
        fields = line.strip().split(";")
        # Check if the sixth field is "PF" or "BCN"
        if fields[5] in ["PF", "BCN"]:
            # If the field is "PF" or "BCN" we will change the value of the seventh field
            fields[6] = str(random.randint(10000,99999))
            # Write the modified line to the output file
            output_file.write(";".join(fields) + "\n")
