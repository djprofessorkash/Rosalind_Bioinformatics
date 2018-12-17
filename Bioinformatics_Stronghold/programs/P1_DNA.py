"""
NAME:               Counting DNA Nucleotides (Bioinformatics Stronghold)
CONTRIBUTOR:        Aakash Sudhakar

PROBLEM:            A string is simply an ordered collection of symbols selected from some alphabet and formed into a word. 
                    The length of a string is the number of symbols that it contains.
                    
                    An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') 
                    is "ATGCTTCAGAAAGGTCTTACG."

DATASET:            A DNA string s of length at most 1000 nt.
OUTPUT:             Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

SAMPLE DATASET:     AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
SAMPLE OUTPUT:      20 12 17 21

STATUS:             Submission successful. 
"""


from collections import OrderedDict

def count_nucleotides_into_dictogram(total_nucleotides):
    """ Support function that creates ordered dictionary histogram of nucleotide occurrences. """
    dictogram, allowed_nucleotides = dict(), ["A", "C", "G", "T"]

    # Builds dictionary-structured histogram of nucleotide frequencies while checking for appropriate permitted nucleotides
    for nucleotide in total_nucleotides:
        if nucleotide in allowed_nucleotides:
            if nucleotide not in dictogram:
                dictogram[nucleotide] = 1
            else:
                dictogram[nucleotide] += 1
        continue

    # Creates ordered dictionary by key alphabetization and returns values in-line
    return OrderedDict(sorted(dictogram.items(), key=lambda X: X[0]))

def main():
    """ Returns frequencies of nucleotides in order A-C-G-T """
    # NOTE: Requires being in parent repo ('pwd' must return up to directory '/Rosalind_Bioinformatics/Bioinformatics_Stronghold')
    FILEPATHREAD = "./datasets/P1_DNA-dataset.txt"
    FILEPATHWRITE = "./outputs/P1_DNA-output.txt"

    # Reads text data from raw dataset as single-line character string
    with open(FILEPATHREAD, "r") as fr:
        nucleotides = fr.read()

    # Creates ordered dictionary histogram of nucleotide occurrences
    dictogram = count_nucleotides_into_dictogram(nucleotides)

    # Creates output file and writes appropriate response to file and notifies user
    with open(FILEPATHWRITE, "w") as fw:
        fw.write(" ".join(["{}".format(value) for key, value in dictogram.items()]))
        
    return print("\nThe DNA dataset has been processed and the appropriate output has been saved to {}.\n".format(FILEPATHWRITE))

if __name__ == "__main__":
    main()