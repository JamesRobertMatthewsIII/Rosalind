#! python3
"""
Given: A file containing at most 1000 lines.
Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.
"""

def get_even_lines(listed_lines):
    even_lines = []
    for line in listed_lines:
        if (listed_lines.index(line) + 1) % 2 == 0:
            even_lines.append(line)
    return ''.join(even_lines)



def main():
    with open("input5.txt") as f:
        line_list = f.readlines()
    with open("output5.txt", 'w') as f:
        f.write(get_even_lines(line_list))

if __name__ == "__main__":
    main()