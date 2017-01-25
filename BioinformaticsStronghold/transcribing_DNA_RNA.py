#! python3
"""
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string tt corresponding to a coding strand, its transcribed RNA string uu is formed by replacing all
occurrences of 'T' in tt with 'U' in uu.

Given: A DNA string tt having length at most 1000 nt.

Return: The transcribed RNA string of tt.
"""


def dna_to_rna(dna_sequence):
    dna_sequence = dna_sequence.strip()

    rna_sequence = []
    for nucleotide in dna_sequence:
        if nucleotide == 'T':
            nucleotide = 'U'
        rna_sequence.append(nucleotide)

    return ''.join(rna_sequence)



def main():
    with open('transcribing_DNA_RNA_dataset.txt') as f:
        input_dna = f.read()

    with open('transcibing_DNA_RNA_output.txt', 'w') as f:
        f.write(dna_to_rna(input_dna))


if __name__ == "__main__":
    main()
