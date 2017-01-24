#! python3
"""
problem 2:
Given: Two positive integers a and b, each less than 1000.
Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a and b
"""
import sys
def hypotenuse_squared(a, b):
    if a >= 1000 or b >= 1000:
        raise Exception("number(s) greater than 1000")
    elif a <= 0 or b <= 0:
        raise Exception("number(s) is negative")
    return int(a**2 + b**2)

def main():
    with open('input2.txt') as f:
        listed_input = f.read().splitlines()
    for line in listed_input:
        line = line.split(' ')
        a = int(line[0])
        b = int(line[1])

        try:
            print(hypotenuse_squared(a, b))
        except Exception as exc:
            print(str(exc))

if __name__ == "__main__":
    main()
