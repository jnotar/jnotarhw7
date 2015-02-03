exon = open("exons.txt")
for line in exon:
    positions = line.split(',')
    start = positions[0]
    stop = positions[1]
    print("start is " + start + ", stop is " + stop)

genomic_dna = open("genomic_dna.txt").read()
exon = open("exons.txt")
sequence = ""
for line in exon:
    positions = line.split(',')
    start = int(positions[0])
    stop = int(positions[1])
    exons = genomic_dna[start:stop]
    sequence = sequence + exons
    print("coding sequence is: " + sequence)

output = open("final_seq.txt", "w")
output.write(sequence)
output.close()
