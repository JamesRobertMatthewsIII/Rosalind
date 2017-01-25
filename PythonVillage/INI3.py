#! python3
"""
Given: A string s of length at most 200 letters and four integers a, b, c and d.
Return: The slice of this string from indices a through b and c through d (with space in between), inclusively.
"""

def slice_up(input_string, a, b, c, d):
    slice1 = input_string[a:b + 1]           # slice is inclusive
    slice2 = input_string[c:d + 1]
    return "%s %s" % (slice1, slice2)

def main():
    with open("input3.txt") as f:
        lines = f.read().splitlines()

    string_line = lines[0]
    index_line = lines[1]
    index_list = index_line.split(' ')
    a = int(index_list[0])
    b = int(index_list[1])
    c = int(index_list[2])
    d = int(index_list[3])

    print(slice_up(string_line, a, b, c, d))


if __name__ == "__main__":
    main()
