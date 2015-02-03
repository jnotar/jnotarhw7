dna = open("input.txt")
dna_out = open("output.txt", "w")

for number in dna:
    trimmings = number[14:]
    dna_out.write(trimmings)
    print("trimmed dna with length " + str(len(trimmings)))
