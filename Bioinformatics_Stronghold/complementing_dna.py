#! python3
"""
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
The reverse complement of a DNA string s is the string s^c formed by reversing the symbols of s,
then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement s^c of s.
"""

def reverse_complement(dna_string):
    '''
    Takes a dna string and returns the reversed and complemented string
    :param dna_string: string
    :return: string
    '''
    dna_string = dna_string.strip()
    complemented_string = []
    for nucleotide in dna_string:
        if nucleotide == 'A':
            complemented_string.append('T')
        elif nucleotide == 'T':
            complemented_string.append('A')
        elif nucleotide == 'C':
            complemented_string.append('G')
        elif nucleotide == 'G':
            complemented_string.append('C')
    return ''.join(complemented_string[::-1])

def main():
    with open('complementing_dna_dataset.txt') as f:
        complemented_dna = reverse_complement(f.readline())
    with open('complementing_dna_output.txt', 'w') as f:
        f.write(complemented_dna)

if __name__ == '__main__':
    main()