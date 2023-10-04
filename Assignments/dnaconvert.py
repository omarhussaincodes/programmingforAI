import json
# DNA code is comprised of four letters: G, T, A, and C. In a strand of DNA, each triplet of these letters is a called
# a codon. Each codon represents an amino acid. Your first task in this tech check is to convert a DNA sequence
# – stored as a string – into the corresponding sequence of codons.

# Step 1
DNA_SEQUENCE_STRING = "GCTCGTAATGATTGT"
CODON_LEN = 3

# without list comprehension
def convert_to_codon_sequence(DNA_SEQUENCE_STRING):
    codons = []
    for i in range(0, len(DNA_SEQUENCE_STRING), CODON_LEN):
        # range 1,3 since codonlength is 3.
        substring = DNA_SEQUENCE_STRING[i:i+CODON_LEN]
        codons.append(substring)
    return codons

# with list comprehension
def dna_seq_to_codon(DNA_SEQUENCE_STRING):
    return [DNA_SEQUENCE_STRING[i:i+CODON_LEN] for i in range(0, len(DNA_SEQUENCE_STRING), CODON_LEN)]

print(convert_to_codon_sequence(DNA_SEQUENCE_STRING))
print(dna_seq_to_codon(DNA_SEQUENCE_STRING))

# codon-sequence
codon_seq = dna_seq_to_codon(DNA_SEQUENCE_STRING)
print(f"Codon Sequence for DNA provided:{codon_seq}")

# Step 2
# reading json data
with open("./dna_data.json", "r") as jsonfile:
    json_data = json.load(jsonfile)
    amino_acids = json_data["amino_acids"]

def convert_codon_to_aminoacid_sequence(codon_sequence):
    result_list = []
    for codon in codon_sequence:
        for aminoacid in amino_acids:
            if (codon in aminoacid["dna_codons"]):
                result_list.append(aminoacid["amino_acid_name"])

    return result_list

amino_acid_sequence = convert_codon_to_aminoacid_sequence(codon_seq)
print(f"Amino Acid sequence for codon sequence: {amino_acid_sequence}")
