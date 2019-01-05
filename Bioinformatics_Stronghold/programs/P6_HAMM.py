"""
NAME:               Counting Point Mutations (Bioinformatics Stronghold)
CONTRIBUTOR:        Aakash Sudhakar

PROBLEM:            Given two strings s and t of equal length, the Hamming distance 
                    between s and t, denoted dH(s,t), is the number of corresponding 
                    symbols that differ in s and t.

DATASET:            Two DNA strings s and t of equal length (not exceeding 1 kbp).
OUTPUT:             The Hamming distance dH(s,t).

SAMPLE DATASET:     GAGCCTACTAACGGGAT
                    CATCGTAATGACGGCCT

SAMPLE OUTPUT:      7

STATUS:             Submission successful. 
"""

def calculate_Hamming_distance(S, T):
    """ Calculates Hamming distance using DNA string inputs. """
    return sum(1 for char_S, char_T in zip(S, T) if char_S != char_T)

def main():
    # NOTE: Requires being in parent repo ('pwd' must return up to directory '/Rosalind_Bioinformatics/Bioinformatics_Stronghold')
    FILEPATHREAD = "./datasets/P6_HAMM-dataset.txt"
    FILEPATHWRITE = "./outputs/P6_HAMM-output.txt"

    # Reads text data from raw dataset as single-line array of characters
    with open(FILEPATHREAD, "r") as fr:
        data = fr.readlines()
        
    # Grabs DNA string parameters from dataset
    S, T = data[0], data[1]

    # Creates output file and writes appropriate response to file and notifies user
    with open(FILEPATHWRITE, "w") as fw:
        fw.write(str(calculate_Hamming_distance(S, T)))

    return print("\nThe DNA Hamming Distance dataset has been processed and the appropriate output has been saved to {}.\n".format(FILEPATHWRITE))

if __name__ == "__main__":
    main()