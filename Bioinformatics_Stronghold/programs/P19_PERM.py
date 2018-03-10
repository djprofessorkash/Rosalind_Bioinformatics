"""
NAME:               Enumerating Gene Orders (Bioinformatics Stronghold)
CONTRIBUTOR:        Aakash Sudhakar

PROBLEM:            A permutation of length n is an ordering of the positive 
                    integers {1, 2, …, n}. For example, π = (5, 3, 2, 1, 4) is a 
                    permutation of length 5.

DATASET:            A positive integer n ≤ 7.

OUTPUT:             The total number of permutations of length n, followed by a list 
                    of all such permutations (in any order).

SAMPLE DATASET:     3
SAMPLE OUTPUT:      6
                    1 2 3
                    1 3 2
                    2 1 3
                    2 3 1
                    3 1 2
                    3 2 1

STATUS:             Pending.
"""

def main():
    # NOTE: Requires being in parent repo ('pwd' must return up to directory '/Rosalind_Bioinformatics/Bioinformatics_Stronghold')
    FILEPATHREAD = "./datasets/P19_sample.txt"
    # FILEPATHREAD = "./datasets/P19_PERM-dataset.txt"
    FILEPATHWRITE = "./outputs/P19_PERM-output.txt"

    # Reads text data from raw dataset as single-line array of characters
    with open(FILEPATHREAD, "r") as fr:
        data = fr.read()

    # Creates output file and writes appropriate response to file and notifies user
    with open(FILEPATHWRITE, "w") as fw:
        fw.write(str(data))

    return print("\nThe Gene Orders dataset has been processed and the appropriate output has been saved to {}.\n".format(FILEPATHWRITE[2:]))

if __name__ == "__main__":
    main()