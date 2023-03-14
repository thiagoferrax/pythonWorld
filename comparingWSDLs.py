# Read in the files
with open("RequisicaoService2.wsdl", "r") as file1:
    lines1 = file1.readlines()

with open("RequisicaoService2_new.wsdl", "r") as file2:
    lines2 = file2.readlines()

# Find lines containing the specified strings in both files
strings = ["consolidarExtracaoDebcad", "consolidarDebcad"]
lines1_matches = [line for line in lines1 if any(s in line for s in strings)]
lines2_matches = [line for line in lines2 if any(s in line for s in strings)]

# Print the matching lines from each file
print("Matches in File 1:")
for line in lines1_matches:
    print(line.strip())

print("\nMatches in File 2:")
for line in lines2_matches:
    print(line.strip())