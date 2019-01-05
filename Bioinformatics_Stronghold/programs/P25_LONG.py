"""
NAME:               Genome Assembly as Shortest Superstring (Bioinformatics Stronghold)
CONTRIBUTOR:        Aakash Sudhakar

PROBLEM:            For a collection of strings, a larger string containing every one 
                    of the smaller strings as a substring is called a superstring.

                    By the assumption of parsimony, a shortest possible superstring 
                    over a collection of reads serves as a candidate chromosome.

DATASET:            At most 50 DNA strings of approximately equal length, not exceeding 1 kbp, 
                    in FASTA format (which represent reads deriving from the same strand 
                    of a single linear chromosome).

                    The dataset is guaranteed to satisfy the following condition: there exists 
                    a unique way to reconstruct the entire chromosome from these reads by 
                    gluing together pairs of reads that overlap by more than half their length.

OUTPUT:             A shortest superstring containing all the given strings (thus corresponding 
                    to a reconstructed chromosome).

SAMPLE DATASET:     >Rosalind_56
                    ATTAGACCTG
                    >Rosalind_57
                    CCTGCCGGAA
                    >Rosalind_58
                    AGACCTGCCG
                    >Rosalind_59
                    GCCGGAATAC

SAMPLE OUTPUT:      ATTAGACCTGCCGGAATAC

STATUS:             Pending.
"""

def main():
    # NOTE: Requires being in parent repo ('pwd' must return up to directory '/Rosalind_Bioinformatics/Bioinformatics_Stronghold')
    FILEPATHREAD = "./datasets/P25_LONG-sample.txt"
    # FILEPATHREAD = "./datasets/P25_LONG-dataset.txt"
    FILEPATHWRITE = "./outputs/P25_LONG-output.txt"

    # Reads text data from raw dataset
    with open(FILEPATHREAD, "r") as fr:
        data = fr.read()
    
    # Creates output file and writes appropriate response to file and notifies user
    with open(FILEPATHWRITE, "w") as fw:
        fw.write(str(data))

    return print("\nThe Shortest Superstrings dataset has been processed and the appropriate output has been saved to {}.\n".format(FILEPATHWRITE[2:]))

if __name__ == "__main__":
    main()