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

                    NOTE: Script contains two implementations: one using a dictionary holding
                    RNA-to-protein conversions as key-value pairs, and other using tree
                    traversals to produce codons per individual base translations. 

DATASET:            An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

OUTPUT:             The protein string encoded by s.

SAMPLE DATASET:     AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
SAMPLE OUTPUT:      MAMAPRTEINSTRING

STATUS:             Submitted, additional work available.
"""


def protein_translation_with_table(data):
    translation_table = {
        "UUU": "F",      "CUU": "L",      "AUU": "I",      "GUU": "V",
        "UUC": "F",      "CUC": "L",      "AUC": "I",      "GUC": "V",
        "UUA": "L",      "CUA": "L",      "AUA": "I",      "GUA": "V",
        "UUG": "L",      "CUG": "L",      "AUG": "M",      "GUG": "V",
        "UCU": "S",      "CCU": "P",      "ACU": "T",      "GCU": "A",
        "UCC": "S",      "CCC": "P",      "ACC": "T",      "GCC": "A",
        "UCA": "S",      "CCA": "P",      "ACA": "T",      "GCA": "A",
        "UCG": "S",      "CCG": "P",      "ACG": "T",      "GCG": "A",
        "UAU": "Y",      "CAU": "H",      "AAU": "N",      "GAU": "D",
        "UAC": "Y",      "CAC": "H",      "AAC": "N",      "GAC": "D",
        "UAA": "Stop",   "CAA": "Q",      "AAA": "K",      "GAA": "E",
        "UAG": "Stop",   "CAG": "Q",      "AAG": "K",      "GAG": "E",
        "UGU": "C",      "CGU": "R",      "AGU": "S",      "GGU": "G",
        "UGC": "C",      "CGC": "R",      "AGC": "S",      "GGC": "G",
        "UGA": "Stop",   "CGA": "R",      "AGA": "R",      "GGA": "G",
        "UGG": "W",      "CGG": "R",      "AGG": "R",      "GGG": "G"
    }
    protein_chain = str()
    for iterator in range(0, len(data), 3):
        codon = data[iterator:iterator+3]
        if translation_table[codon] == "Stop":
            return protein_chain
        protein_chain += translation_table[codon]

def protein_translation_with_tree(data):
    pass

def main():
    # NOTE: Requires being in parent repo ('pwd' must return up to directory '/Rosalind_Bioinformatics/Bioinformatics_Stronghold')
    FILEPATHREAD = "./datasets/P8_PROT-dataset.txt"
    FILEPATHWRITE = "./outputs/P8_PROT-output.txt"

    # Reads text data from raw dataset as single-line array of characters
    with open(FILEPATHREAD, "r") as fr:
        data = fr.read()

    # Creates output file and writes appropriate response to file and notifies user
    with open(FILEPATHWRITE, "w") as fw:
        fw.write(str(protein_translation_with_table(data)))

    return print("\nThe RNA Translation dataset has been processed and the appropriate output has been saved to {}.\n".format(FILEPATHWRITE))

if __name__ == "__main__":
    main()