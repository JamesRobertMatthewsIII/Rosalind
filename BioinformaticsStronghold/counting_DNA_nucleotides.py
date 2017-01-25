#! python3
"""
A string is simply an ordered collection of symbols selected from some alphabet and formed into a word;
the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is
"ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string ss of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols
'A', 'C', 'G', and 'T' occur in s.
"""


def count_nucleotides(dna_string):
    """
    counts nucleotides in a DNA sequence and returns a dictionary with the number of occurences of each nucleotide.
    :param dna_string: string
    :return: dictionary
    """
    nucleotide_count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for nucleotide in nucleotide_count.keys():
        nucleotide_count[nucleotide] = dna_string.count(nucleotide)
    return nucleotide_count

def main():
    with open('counting_DNA_nucleotides_dataset.txt') as f:
        dna_sequence = f.read().strip()

    with open('counting_DNA_nucleotides_output.txt', 'w') as f:
        for nucleotide in ['A', 'C', 'G', 'T']:
            f.write("%s " % str(count_nucleotides(dna_sequence)[nucleotide]))

if __name__ == "__main__":
    main()