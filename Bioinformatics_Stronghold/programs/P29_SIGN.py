"""
NAME:               Enumerating Oriented Gene Orderings (Bioinformatics Stronghold)
CONTRIBUTOR:        Aakash Sudhakar

PROBLEM:            A signed permutation of length N is some ordering of the positive 
                    integers {1, 2, ..., n} in which each integer is then provided 
                    with either a positive or negative sign (for the sake of simplicity, 
                    we omit the positive sign). For example, π = (5, −3, −2, 1, 4) is 
                    a signed permutation of length 5.

DATASET:            A positive integer n ≤ 6.

OUTPUT:             The total number of signed permutations of length n, followed by a list 
                    of all such permutations (you may list the signed permutations in any order).

SAMPLE DATASET:     2

SAMPLE OUTPUT:      8
                    -1 -2
                    -1 2
                    1 -2
                    1 2
                    -2 -1
                    -2 1
                    2 -1
                    2 1

STATUS:             Pending.
"""

def main():
    # NOTE: Requires being in parent repo ('pwd' must return up to directory '/Rosalind_Bioinformatics/Bioinformatics_Stronghold')
    FILEPATHREAD = "./datasets/P29_SIGN-sample.txt"
    # FILEPATHREAD = "./datasets/P29_SIGN-dataset.txt"
    FILEPATHWRITE = "./outputs/P29_SIGN-output.txt"

    # Reads text data from raw dataset
    with open(FILEPATHREAD, "r") as fr:
        data = fr.read()
    
    # Creates output file and writes appropriate response to file and notifies user
    with open(FILEPATHWRITE, "w") as fw:
        fw.write(str(data))

    return print("\nThe Oriented Genes dataset has been processed and the appropriate output has been saved to {}.\n".format(FILEPATHWRITE[2:]))

if __name__ == "__main__":
    main()