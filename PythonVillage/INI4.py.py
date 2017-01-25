#! python3
"""
Given: Two positive integers a and b (a<b<10000a<b<10000).
Return: The sum of all odd integers from a through b, inclusively.
"""

def positive_integers(a, b):
    a_sum = 0
    for num in range(a, b):
        if num % 2 != 0:
            a_sum += num

    return a_sum

def main():
    with open('input4.txt') as f:
        input_line = [line.rstrip() for line in f]
    a = int(input_line[0].split(' ')[0])
    b = int(input_line[0].split(' ')[1])
    print(positive_integers(a, b))

if __name__ == "__main__":
    main()
