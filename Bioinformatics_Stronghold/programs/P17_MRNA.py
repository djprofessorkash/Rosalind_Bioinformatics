"""
NAME:               Inferring mRNA from Protein (Bioinformatics Stronghold)
CONTRIBUTOR:        Aakash Sudhakar

PROBLEM:            For positive integers a and n, a modulo n (written a mod n in shorthand) 
                    is the remainder when a is divided by n. For example, 29 mod 11 = 7 
                    because 29 = 11 × 2 + 7.

                    Modular arithmetic is the study of addition, subtraction, multiplication, 
                    and division with respect to the modulo operation. We say that a and b 
                    are congruent modulo n if a mod n = b mod n; in this case, we use the 
                    notation a ≡ b mod n.

                    Two useful facts in modular arithmetic are that if a ≡ b mod n and 
                    c ≡ d mod n, then a + c ≡ b + d mod n and a × c ≡ b × d mod n. 
                    To check your understanding of these rules, you may wish to verify 
                    these relationships for a = 29, b = 73, c = 10, d = 32, and n = 11.

                    As you will see in this exercise, some Rosalind problems will ask for 
                    a (very large) integer solution modulo a smaller number to avoid the 
                    computational pitfalls that arise with storing such large numbers.

DATASET:            A protein string of length at most 1000 aa.

OUTPUT:             The total number of different RNA strings from which the protein 
                    could have been translated, modulo 1,000,000. 
                    (Don't neglect the importance of the stop codon in protein translation.)

SAMPLE DATASET:     MA
SAMPLE OUTPUT:      12

STATUS:             Pending.
"""

def _codon_dictogram_constructor():
    """ Constructs frequency table for amino-acid-to-protein conversions. """
    codon_dictogram, CODON_TRANSLATION_TABLE = dict(), {
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
    for _, amino_acid in CODON_TRANSLATION_TABLE.items():
        if amino_acid not in codon_dictogram:
            codon_dictogram[amino_acid] = 0
        codon_dictogram[amino_acid] += 1
    return codon_dictogram

def sequence_variations_calculator(protein_chain):
    """ Calculates all possible amino acid variations to generate input protein chain. """
    CODON_FREQS, N = _codon_dictogram_constructor(), 1000000
    possible_variations = CODON_FREQS["Stop"]
    for amino_acid in protein_chain:
        possible_variations *= CODON_FREQS[amino_acid]
    return possible_variations % N

def main():
    # NOTE: Requires being in parent repo ('pwd' must return up to directory '/Rosalind_Bioinformatics/Bioinformatics_Stronghold')
    FILEPATHREAD = "./datasets/P17_MRNA-sample.txt"
    # FILEPATHREAD = "./datasets/P17_MRNA-dataset.txt"
    FILEPATHWRITE = "./outputs/P17_MRNA-output.txt"

    # Reads text data from raw dataset as single-line array of characters
    with open(FILEPATHREAD, "r") as fr:
        data = fr.read().strip()

    # Calculates total sequence variations constructed from possible RNA combinations
    sequence_variations = sequence_variations_calculator(data)

    # Creates output file and writes appropriate response to file and notifies user
    with open(FILEPATHWRITE, "w") as fw:
        fw.write(str(sequence_variations))

    return print("\nThe Protein-to-mRNA dataset has been processed and the appropriate output has been saved to {}.\n".format(FILEPATHWRITE[2:]))

if __name__ == "__main__":
    main()