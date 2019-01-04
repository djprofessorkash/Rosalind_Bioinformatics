"""
NAME:               Calculating Protein Mass (Bioinformatics Stronghold)
CONTRIBUTOR:        Aakash Sudhakar

PROBLEM:            In a weighted alphabet, every symbol is assigned a positive real number 
                    called a weight. A string formed from a weighted alphabet is called a 
                    weighted string, and its weight is equal to the sum of the weights of 
                    its symbols.

                    The standard weight assigned to each member of the 20-symbol amino acid 
                    alphabet is the monoisotopic mass of the corresponding amino acid.

DATASET:            A protein string P of length at most 1000 aa.

OUTPUT:             The total weight of P. Consult a monoisotopic mass table.

SAMPLE DATASET:     SKADYEK
SAMPLE OUTPUT:      821.392

STATUS:             Submission successful.
"""

def calculate_protein_sequence_mass(protein_sequence):
    """ Calculates total protein sequence mass using monoisotopic mass lookup table. """
    MONOISOTOPIC_MASS_TABLE = {
        "A": 71.03711, 
        "C": 103.00919,
        "D": 115.02694,
        "E": 129.04259,
        "F": 147.06841,
        "G": 57.02146,
        "H": 137.05891,
        "I": 113.08406,
        "K": 128.09496,
        "L": 113.08406,
        "M": 131.04049,
        "N": 114.04293,
        "P": 97.05276,
        "Q": 128.05858,
        "R": 156.10111,
        "S": 87.03203,
        "T": 101.04768,
        "V": 99.06841,
        "W": 186.07931,
        "Y": 163.06333
    }
    return sum([MONOISOTOPIC_MASS_TABLE[amino_acid] for amino_acid in protein_sequence])

def main():
    # NOTE: Requires being in parent repo ('pwd' must return up to directory '/Rosalind_Bioinformatics/Bioinformatics_Stronghold')
    FILEPATHREAD = "./datasets/P20_PRTM-dataset.txt"
    FILEPATHWRITE = "./outputs/P20_PRTM-output.txt"

    # Reads text data from raw dataset as single-line array of characters
    with open(FILEPATHREAD, "r") as fr:
        data = list(fr.read().strip())

    # Calculates total protein sequence mass using monoisotopic lookup table
    protein_sequence_mass = round(calculate_protein_sequence_mass(data), 3)

    # Creates output file and writes appropriate response to file and notifies user
    with open(FILEPATHWRITE, "w") as fw:
        fw.write(str(protein_sequence_mass))

    return print("\nThe Protein Masses dataset has been processed and the appropriate output has been saved to {}.\n".format(FILEPATHWRITE[2:]))

if __name__ == "__main__":
    main()