"""
NAME:               Locating Restriction Sites (Bioinformatics Stronghold)
CONTRIBUTOR:        Aakash Sudhakar

PROBLEM:            A DNA string is a reverse palindrome if it is equal to its 
                    reverse complement. For instance, GCATGC is a reverse palindrome 
                    because its reverse complement is GCATGC. 

DATASET:            A DNA string of length at most 1 kbp in FASTA format.

OUTPUT:             The position and length of every reverse palindrome in the string 
                    having length between 4 and 12. You may return these pairs in any order.

SAMPLE DATASET:     >Rosalind_24
                    TCAATGCATGCGGGTCTATATGCAT

SAMPLE OUTPUT:      4 6
                    5 4
                    6 6
                    7 4
                    17 4
                    18 4
                    20 6
                    21 4

STATUS:             Pending.
"""

def main():
    # NOTE: Requires being in parent repo ('pwd' must return up to directory '/Rosalind_Bioinformatics/Bioinformatics_Stronghold')
    FILEPATHREAD = "./datasets/P21_sample.txt"
    # FILEPATHREAD = "./datasets/P21_REVP-dataset.txt"
    FILEPATHWRITE = "./outputs/P21_REVP-output.txt"

    # Reads text data from raw dataset as single-line array of characters
    with open(FILEPATHREAD, "r") as fr:
        data = fr.read()

    # Creates output file and writes appropriate response to file and notifies user
    with open(FILEPATHWRITE, "w") as fw:
        fw.write(str(data))

    return print("\nThe Restriction Sites dataset has been processed and the appropriate output has been saved to {}.\n".format(FILEPATHWRITE[2:]))

if __name__ == "__main__":
    main()