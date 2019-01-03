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

STATUS:             In progress.
"""

def calculate_protein_sequence_mass(protein_sequence):
    pass

def main():
    # NOTE: Requires being in parent repo ('pwd' must return up to directory '/Rosalind_Bioinformatics/Bioinformatics_Stronghold')
    FILEPATHREAD = "./datasets/P20_PRTM-sample.txt"
    # FILEPATHREAD = "./datasets/P20_PRTM-dataset.txt"
    FILEPATHWRITE = "./outputs/P20_PRTM-output.txt"

    # Reads text data from raw dataset as single-line array of characters
    with open(FILEPATHREAD, "r") as fr:
        data = fr.read()

    # Creates output file and writes appropriate response to file and notifies user
    with open(FILEPATHWRITE, "w") as fw:
        fw.write(str(calculate_protein_sequence_mass(data)))

    return print("\nThe Protein Masses dataset has been processed and the appropriate output has been saved to {}.\n".format(FILEPATHWRITE[2:]))

if __name__ == "__main__":
    main()