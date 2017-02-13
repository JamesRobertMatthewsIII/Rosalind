#! python3
'''
Identifying unknown DNA quickly

The GC-content of a DNA string is given by the percentage of symbols in the string
that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note
that the reverse complement of any DNA string has the same GC-content.

DNA strings must be labeled when they are consolidated into a database. A commonly
used method of string labeling is called FASTA format. In this format, the string
is introduced by a line that begins with '>', followed by some labeling information.
Subsequent lines contain the string itself; the first line to begin with '>'
indicates the label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the ID
"Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the
GC-content of that string. Rosalind allows for a default error of 0.001 in all
decimal answers unless otherwise stated; please see the note on absolute error below.
'''
import re


def parse_input(dataset):
    '''
    takes DNA strings in FASTA format and returns a dictionary with
    { ID: GC percentage}
    :param dataset: string
    :return: dictionary
    '''

    FASTA_REGEX = re.compile(r'(>\w+)\n([GCTA\n]+)')
    match_list = FASTA_REGEX.findall(dataset, re.DOTALL)

    match_dict = {}
    for match in match_list:
        identification = match[0]
        dna_string = match[1]

        # have to remove the newlines in dna_string
        dna_string = dna_string.replace('\n', '')

        # have to remove the '>' from id
        identification = identification.replace('>', '')

        gc_counter = 0
        for nucleotide in dna_string:
            if nucleotide in 'GC':
                gc_counter += 1

        gc_percentage = (gc_counter / float(len(dna_string)) * 100)
        match_dict[identification] = gc_percentage
    return match_dict

def get_largest_percentage(dna_dict):
    '''
    takes a dictionary of the form { id: percentage }, returns string with the
    id on one line and the percentage on the next
    :param dna_dict: dictionary
    :return: string
    '''
    # get the largest value in the dictionary
    largest = sorted(list(dna_dict.values()))[-1]

    eps = 0.001
    for id_num, percentage in dna_dict.items():
        if abs(percentage - largest) <= eps:
            return '{}\n{}'.format(id_num, str(percentage))
    return 'change epsilon'

def main():
    with open('quick_dna_id_dataset.txt') as f:
        string_input = f.read()

    with open('quick_dna_id_output.txt', 'w') as f:
        f.write(get_largest_percentage(parse_input(string_input)))

if __name__ == '__main__':
    main()
