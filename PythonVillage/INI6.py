#! python3
"""
Given: A string ss of length at most 10000 letters.
Return: How many times any word occurred in string. Each letter case (upper or lower) in word matters.
        Lines in output can be in any order.
"""

def count_words(input_string):
    word_dict = {}
    for word in input_string.strip().split(' '):
        if word == ' ':
            continue
        elif word in word_dict.keys():
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict


def main():
    with open('input6.txt') as f:
        file_string = f.read()
    with open('output6.txt', 'w') as f:
        for word, count in count_words(file_string).items():
            f.write("%s %s\n" % (word, str(count)))

if __name__ == "__main__":
    main()



