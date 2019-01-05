"""
NAME:               Finding a Spliced Motif (Bioinformatics Stronghold)
CONTRIBUTOR:        Aakash Sudhakar

PROBLEM:            A subsequence of a string is a collection of symbols contained in order 
                    (though not necessarily contiguously) in the string (e.g., ACG is 
                    a subsequence of TATGCTAAGATC). The indices of a subsequence are 
                    the positions in the string at which the symbols of the subsequence appear; 
                    thus, the indices of ACG in TATGCTAAGATC can be represented by (2, 5, 9).

                    As a substring can have multiple locations, a subsequence can have 
                    multiple collections of indices, and the same index can be reused 
                    in more than one appearance of the subsequence; for example, ACG is 
                    a subsequence of AACCGGTT in 8 different ways.

DATASET:            Two DNA strings S and T (each of length at most 1 kbp) in FASTA format.

OUTPUT:             One collection of indices of S in which the symbols of T appear 
                    as a subsequence of s. If multiple solutions exist, you may return any one.

SAMPLE DATASET:     >Rosalind_14
                    ACGTACGTGACG
                    >Rosalind_18
                    GTA

SAMPLE OUTPUT:      3 8 10

STATUS:             Pending.
"""

def main():
    # NOTE: Requires being in parent repo ('pwd' must return up to directory '/Rosalind_Bioinformatics/Bioinformatics_Stronghold')
    FILEPATHREAD = "./datasets/P30_SSEQ-sample.txt"
    # FILEPATHREAD = "./datasets/P30_SSEQ-dataset.txt"
    FILEPATHWRITE = "./outputs/P30_SSEQ-output.txt"

    # Reads text data from raw dataset
    with open(FILEPATHREAD, "r") as fr:
        data = fr.read()
    
    # Creates output file and writes appropriate response to file and notifies user
    with open(FILEPATHWRITE, "w") as fw:
        fw.write(str(data))

    return print("\nThe Spliced Motifs dataset has been processed and the appropriate output has been saved to {}.\n".format(FILEPATHWRITE[2:]))

if __name__ == "__main__":
    main()