"""
NAME:               RNA Splicing (Bioinformatics Stronghold)
CONTRIBUTOR:        Aakash Sudhakar

PROBLEM:            After identifying the exons and introns of an RNA string, we only need 
                    to delete the introns and concatenate the exons to form a new string 
                    ready for translation.

DATASET:            A DNA string s (of length at most 1 kbp) and a collection of substrings 
                    of s acting as introns. All strings are given in FASTA format.

OUTPUT:             A protein string resulting from transcribing and translating the exons 
                    of s. (Note: Only one solution will exist for the dataset provided.)

SAMPLE DATASET:     >Rosalind_10
                    ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
                    >Rosalind_12
                    ATCGGTCGAA
                    >Rosalind_15
                    ATCGGTCGAGCGTGT

SAMPLE OUTPUT:      MVYIADKQHVASREAYGHMFKVCA

STATUS:             Pending.
"""

def main():
    # NOTE: Requires being in parent repo ('pwd' must return up to directory '/Rosalind_Bioinformatics/Bioinformatics_Stronghold')
    FILEPATHREAD = "./datasets/P22_sample.txt"
    # FILEPATHREAD = "./datasets/P22_SPLC-dataset.txt"
    FILEPATHWRITE = "./outputs/P22_SPLC-output.txt"

    # Reads text data from raw dataset as single-line array of characters
    with open(FILEPATHREAD, "r") as fr:
        data = fr.read()

    # Creates output file and writes appropriate response to file and notifies user
    with open(FILEPATHWRITE, "w") as fw:
        fw.write(str(data))

    return print("\nThe RNA Splicing dataset has been processed and the appropriate output has been saved to {}.\n".format(FILEPATHWRITE[2:]))

if __name__ == "__main__":
    main()