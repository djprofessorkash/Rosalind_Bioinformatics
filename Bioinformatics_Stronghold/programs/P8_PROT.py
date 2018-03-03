"""
NAME:               Translating RNA into Protein (Bioinformatics Stronghold)
CONTRIBUTOR:        Aakash Sudhakar

PROBLEM:            The 20 commonly occurring amino acids are abbreviated by using 20 letters 
                    from the English alphabet (all letters except for B, J, O, U, X, and Z). 
                    Protein strings are constructed from these 20 symbols. Henceforth, 
                    the term genetic string will incorporate protein strings along 
                    with DNA strings and RNA strings.

                    The RNA codon table dictates the details regarding the encoding of 
                    specific codons into the amino acid alphabet.

DATASET:            An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

OUTPUT:             The protein string encoded by s.

SAMPLE DATASET:     AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
SAMPLE OUTPUT:      MAMAPRTEINSTRING

STATUS:             Incomplete.
"""


def translation_tree():
    pass

def main():
    # NOTE: Requires being in parent repo ('pwd' must return up to directory '/Rosalind_Bioinformatics/Bioinformatics_Stronghold')
    # FILEPATHREAD = "./datasets/P8_PROT-dataset.txt"
    FILEPATHREAD = "./datasets/P8_example.txt"
    FILEPATHWRITE = "./outputs/P8_PROT-output.txt"

    # Reads text data from raw dataset as single-line array of characters
    with open(FILEPATHREAD, "r") as fr:
        data = fr.read()

    

    # Creates output file and writes appropriate response to file and notifies user
    with open(FILEPATHWRITE, "w") as fw:
        fw.write()

    return print("\nThe RNA Translation dataset has been processed and the appropriate output has been saved to {}.\n".format(FILEPATHWRITE))

if __name__ == "__main__":
    main()