"""
NAME:               Complementing a Strand of DNA (Bioinformatics Stronghold)
CONTRIBUTOR:        Aakash Sudhakar

PROBLEM:            In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
                    
                    The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then 
                    taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

DATASET:            A DNA string s of length at most 1000 bp.
OUTPUT:             The reverse complement of DNA string s.

SAMPLE DATASET:     AAAACCCGGT
SAMPLE OUTPUT:      ACCGGGTTTT

STATUS:             Submission successful. 
"""

def produce_reverse_complement(nucleotide_collection):
    """ Produces reverse complement strand from DNA nucleotides. """
    BASE_PAIRS = {"A": "T", "T": "A", "G": "C", "C": "G"}
    return [str(nucleotide) for nucleotide in [BASE_PAIRS.get(key) for key in nucleotide_collection.strip()]]

def main():
    """ Returns new string transposed back-to-front and with swapped base pairs (A-T, C-G) """    
    # NOTE: Requires being in parent repo ('pwd' must return up to directory '/Rosalind_Bioinformatics/Bioinformatics_Stronghold')
    FILEPATHREAD = "./datasets/P3_REVC-dataset.txt"
    FILEPATHWRITE = "./outputs/P3_REVC-output.txt"

    # Reads text data from raw dataset as single-line array of characters
    with open(FILEPATHREAD, "r") as fr:
        original_strand = fr.read()

    # Creates output file and writes appropriate response to file and notifies user
    with open(FILEPATHWRITE, "w") as fw:
        fw.write("".join(produce_reverse_complement(original_strand))[::-1])

    return print("\nThe complementary DNA dataset has been processed and the appropriate output has been saved to {}.\n".format(FILEPATHWRITE))


if __name__ == "__main__":
    main()