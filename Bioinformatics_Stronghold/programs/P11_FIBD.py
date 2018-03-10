"""
NAME:               Mortal Fibonacci Rabbits (Bioinformatics Stronghold)
CONTRIBUTOR:        Aakash Sudhakar

PROBLEM:            Recall the definition of the Fibonacci numbers from 
                    “Rabbits and Recurrence Relations”, which followed the 
                    recurrence relation F_{n} = F_{n-1} + F_{n-2} and 
                    assumed that each pair of rabbits reaches maturity in one month 
                    and produces a single pair of offspring (one male, one female) 
                    each subsequent month.

                    Our aim is to somehow modify this recurrence relation to achieve 
                    a dynamic programming solution in the case that all rabbits die out 
                    after a fixed number of months.

DATASET:            Positive integers n ≤ 100 and m ≤ 20.

OUTPUT:             The total number of pairs of rabbits that will remain after 
                    the n-th month if all rabbits live for m months.

SAMPLE DATASET:     6 3
SAMPLE OUTPUT:      4

STATUS:             Pending.
"""

def mortal_recurrence_relation_polynomial(n, m):
    """ Calculates Fibonacci sequence with mortality rate m and returns total offspring
    after n months. (Polynomial Method) """
    pass

def mortal_recurrence_relation_recursive(n, m):
    """ Calculates Fibonacci sequence with mortality rate m and returns total offspring
    after n months. (Recursive Method)"""
    # NOTE: Recursive method quickly breaks down due to timeout at larger values of n and m.
    if n <= 100 and m <= 20:
        if n == 0:
            # Standard Fibonacci Boundary Condition
            return 0
        if n == 1:
            # Standard Fibonacci Boundary Condition
            return 1
        if n <= m:
            # Standard Fibonacci General Logic
            return mortal_recurrence_relation_recursive(n - 1, m) + mortal_recurrence_relation_recursive(n - 2, m)
        elif n == m + 1:
            # Account for mortality with f(n - (m + 1), m) where n == m, therefore f == -1
            return mortal_recurrence_relation_recursive(n - 1, m) + mortal_recurrence_relation_recursive(n - 2, m) - 1
        else:
            # Account for general mortality with f(n - (m + 1), m) where n != m
            return mortal_recurrence_relation_recursive(n - 1, m) + mortal_recurrence_relation_recursive(n - 2, m) - mortal_recurrence_relation_recursive(n - (m + 1), m)
    else:
        raise ValueError("\n\nFUNCTION PARAMETERS ARE TOO LARGE TO HANDLE.\n\nn <= 100 (CURRENT: n = {})\nm <= 20 (CURRENT: m = {})\n".format(n, m))

def mortal_recurrence_relation_iterative(n, m):
    """ Calculates Fibonacci sequence with mortality rate m and returns total offspring
    after n months. (Iterative Method) """
    if n <= 100 or m <= 20:
        mortal_fibonacci_series, months_elapsed = [1, 1], 2     # Initializes rabbit pairs
        while months_elapsed < n:
            fibrr_iter1, fibrr_iter2 = mortal_fibonacci_series[-2], mortal_fibonacci_series[-1]

            if months_elapsed < m:
                mortal_fibonacci_series.append(fibrr_iter1 + fibrr_iter2)
            elif months_elapsed == m:
                mortal_fibonacci_series.append(fibrr_iter1 + fibrr_iter2 - 1)
            else:
                fibrr_mortal = mortal_fibonacci_series[-(m + 1)]
                mortal_fibonacci_series.append(fibrr_iter1 + fibrr_iter2 - fibrr_mortal)
            
            months_elapsed += 1
        return mortal_fibonacci_series[-1]
    else:
        raise ValueError("\n\nFUNCTION PARAMETERS ARE TOO LARGE TO HANDLE.\n\nn <= 100 (CURRENT: n = {})\nm <= 20 (CURRENT: m = {})\n".format(n, m))

def main():
    # NOTE: Requires being in parent repo ('pwd' must return up to directory '/Rosalind_Bioinformatics/Bioinformatics_Stronghold')
    FILEPATHREAD = "./datasets/P11_FIBD-dataset.txt"
    FILEPATHWRITE = "./outputs/P11_FIBD-output.txt"

    # Reads text data from raw dataset as single-line array of characters
    with open(FILEPATHREAD, "r") as fr:
        n, m = [int(data) for data in fr.read().split(" ")]

    # Creates output file and writes appropriate response to file and notifies user
    with open(FILEPATHWRITE, "w") as fw:
        fw.write(str(mortal_recurrence_relation_iterative(n, m)))

    return print("\nThe Mortal Rabbits dataset has been processed and the appropriate output has been saved to {}.\n".format(FILEPATHWRITE))

if __name__ == "__main__":
    main()