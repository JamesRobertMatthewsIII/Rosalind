#! python3
"""
Description: http://rosalind.info/problems/fib/

Given: Positive integers n≤40n≤40 and k≤5k≤5.

Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation,
every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
"""

def rabbit_pairs_present(months, litter_size):
    """
    takes the number of months and the litter-size, and returns the total number of rabbit pairs that will be present
    :param months: positive integer
    :param litter_size: positive integer
    :return:
    """
    if months == 0:
        return 0
    elif months == 1:
        return 1
    # F(n-1,k) + k*F(n-2,k);
    else:
        return (rabbit_pairs_present(months - 1, litter_size) + litter_size * rabbit_pairs_present(months - 2, litter_size))

def main():
    with open('rabbits_and_recurrence_dataset.txt') as f:
        input_list = f.readline().strip().split(' ')
        n, k = (int(input_list[0]), int(input_list[1]))

    with open('rabbits_and_recurrence_output.txt', 'w') as f:
        f.write(str(rabbit_pairs_present(n, k)))

if __name__ == '__main__':
    main()