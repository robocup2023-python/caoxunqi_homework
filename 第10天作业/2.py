#热爱学习的CXQ

codon_dict = {}
with open('codon.txt', 'r') as codon_file:
    for line in codon_file:
        codon, amino_acid = line.strip().split()
        if codon == 'stop':
            break
        codon_dict[codon] = amino_acid
    del codon_dict['codon']

print(codon_dict)

def transcript(dna_sequence):
    return dna_sequence.replace('T', 'U')

def translate(dna_sequence):
    mrna_sequence = transcript(dna_sequence)
    protein_sequence = ""
    start_codon_found = False

    for i in range(0, len(mrna_sequence), 3):
        codon = mrna_sequence[i:i + 3]

        if codon == "AUG" and not start_codon_found:
            start_codon_found = True
            protein_sequence += codon_dict.get(codon, "")
        elif start_codon_found and codon in codon_dict:
            amino_acid = codon_dict[codon]
            if amino_acid != "stop":
                protein_sequence += amino_acid
            else:
                break

    return protein_sequence

seq_dict = {}
with open('seq.fa', 'r') as seq_file:
    lines = seq_file.readlines()
    current_sequence = ""
    for line in lines:
        if line.startswith('>'):
            if current_sequence:
                seq_dict[sequence_name] = current_sequence
            sequence_name = line.strip().lstrip('>')
            current_sequence = ""
        else:
            current_sequence += line.strip()
    seq_dict[sequence_name] = current_sequence

protein_dict = {}
for sequence_name, dna_sequence in seq_dict.items():
    protein_sequence = translate(dna_sequence)
    protein_dict[sequence_name] = protein_sequence

for sequence_name, protein_sequence in protein_dict.items():
    print(f"{sequence_name}: {protein_sequence}")






