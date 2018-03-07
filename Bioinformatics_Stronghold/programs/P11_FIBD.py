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


# NOTE: It always takes two months (generations) for an infant pair to grow up and have kids.

def mortal_recurrence_relation(n, m):
    """ Calculates fibonacci sequence with mortality rate m and returns total offspring
    after n months. """
    if n <= 100 or m <= 20:
        if n == 0:
            # Standard Fibonacci Boundary Condition
            return 0
        elif n == 1:
            # Standard Fibonacci Boundary Condition
            return 1
        elif n <= m:
            # Standard Fibonacci General Logic
            return mortal_recurrence_relation(n - 1, m) + mortal_recurrence_relation(n - 2, m)
        elif n == m + 1:
            # Account for mortality with f(n - (m + 1), m) where n == m, therefore f == -1
            return mortal_recurrence_relation(n - 1, m) + mortal_recurrence_relation(n - 2, m) - 1
        else:
            # Account for general mortality with f(n - (m + 1), m) where n != m
            return mortal_recurrence_relation(n - 1, m) + mortal_recurrence_relation(n - 2, m) - mortal_recurrence_relation(n - (m + 1), m)
    else:
        raise ValueError("\n\nFUNCTION PARAMETERS ARE TOO LARGE TO HANDLE.\n\nn <= 100 (CURRENT: n = {})\nm <= 20 (CURRENT: m = {})\n".format(n, m))

def main():
    # NOTE: Requires being in parent repo ('pwd' must return up to directory '/Rosalind_Bioinformatics/Bioinformatics_Stronghold')
    FILEPATHREAD = "./datasets/P11_FIBD-dataset.txt"
    FILEPATHWRITE = "./outputs/P11_FIBD-output.txt"

    # Reads text data from raw dataset as single-line array of characters
    with open(FILEPATHREAD, "r") as fr:
        data = fr.read().split(" ")

    # Creates output file and writes appropriate response to file and notifies user
    with open(FILEPATHWRITE, "w") as fw:
        fw.write(str(mortal_recurrence_relation(int(data[0]), int(data[1]))))

    return print("\nThe Mortal Fibonacci dataset has been processed and the appropriate output has been saved to {}.\n".format(FILEPATHWRITE))

if __name__ == "__main__":
    main()