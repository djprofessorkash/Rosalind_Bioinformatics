"""
NAME:               Partial Permutations (Bioinformatics Stronghold)
CONTRIBUTOR:        Aakash Sudhakar

PROBLEM:            A partial permutation is an ordering of only k objects taken from 
                    a collection containing n objects (i.e., k ≤ n). For example, 
                    one partial permutation of three of the first eight positive integers 
                    is given by (5, 7, 2).

                    The statistic P(n, k) counts the total number of partial permutations 
                    of k objects that can be formed from a collection of n objects. 
                    Note that P(n, n) is just the number of permutations of n objects, 
                    which we found to be equal to n! = n(n − 1)(n − 2)...(3)(2) 
                    in “P19: Enumerating Gene Orders (PERM)”.

DATASET:            Positive integers n and k such that 100 ≥ n > 0 and 10 ≥ k > 0.

OUTPUT:             The total number of partial permutations P(n, k), modulo 1,000,000.

SAMPLE DATASET:     21 7

SAMPLE OUTPUT:      51200

STATUS:             Pending.
"""

def main():
    # NOTE: Requires being in parent repo ('pwd' must return up to directory '/Rosalind_Bioinformatics/Bioinformatics_Stronghold')
    FILEPATHREAD = "./datasets/P27_PPER-sample.txt"
    # FILEPATHREAD = "./datasets/P27_PPER-dataset.txt"
    FILEPATHWRITE = "./outputs/P27_PPER-output.txt"

    # Reads text data from raw dataset
    with open(FILEPATHREAD, "r") as fr:
        data = fr.read()
    
    # Creates output file and writes appropriate response to file and notifies user
    with open(FILEPATHWRITE, "w") as fw:
        fw.write(str(data))

    return print("\nThe Partial Permutations dataset has been processed and the appropriate output has been saved to {}.\n".format(FILEPATHWRITE[2:]))

if __name__ == "__main__":
    main()