"""
NAME:               Introduction to the Bioinformatics Armory (Bioinformatics Armory)
CONTRIBUTOR:        Aakash Sudhakar

PROBLEM:            This initial problem is aimed at familiarizing you with 
                    Rosalind's task-solving pipeline. To solve it, you merely have to 
                    take a given DNA sequence and find its nucleotide counts; this problem 
                    is equivalent to “Counting DNA Nucleotides” in the Stronghold.

                    Of the many tools for DNA sequence analysis, one of the most popular 
                    is the Sequence Manipulation Suite. Commonly known as SMS 2, it comprises 
                    a collection of programs for generating, formatting, and analyzing 
                    short strands of DNA and polypeptides.

                    One of the simplest SMS 2 programs, called DNA stats, counts the number 
                    of occurrences of each nucleotide in a given strand of DNA. 
                    
                    An online interface for DNA stats can be found 
                    at http://www.bioinformatics.org/sms2/dna_stats.html.
                    
DATASET:            A DNA string s of length at most 1000 bp.

OUTPUT:             Four integers (separated by spaces) representing the respective 
                    number of times that the symbols 'A', 'C', 'G', and 'T' occur in s. 
                    
                    NOTE: You must provide your answer in the format shown in the 
                    sample output below.

SAMPLE DATASET:     AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC

SAMPLE OUTPUT:      20 12 17 21

STATUS:             Submission successful.

PYTHON SHORTCUT:    Our default choice for existing functions and modules to analyze 
                    biological data is BioPython, a set of freely available tools 
                    for computational biology that are written in Python. We will give you 
                    tips on how to solve certain problems (like this one) using 
                    BioPython functions and methods.

                    BioPython offers a specific data structure called Seq for 
                    representing sequences. Seq represents an extension of 
                    the "str" (string) object type that is built into Python by supporting 
                    additional biologically relevant methods like `translate()` and 
                    `reverse_complement()`.

                    In this problem, you can easily use the built-in Python method 
                    `.count()` for strings.
"""

from Bio.Seq import Seq

def compute_DNA_nucleotide_counts(dataset):
    target_seq, base_occurrences = Seq(dataset), list()
    for base in ["A", "C", "G", "T"]:
        base_occurrences.append(str(target_seq.count(base)))
    return base_occurrences

def main():
    # NOTE: Requires being in parent repo ('pwd' must return up to directory '/Rosalind_Bioinformatics/Bioinformatics_Armory')
    FILEPATHREAD = "./datasets/P1_INI-dataset.txt"
    FILEPATHWRITE = "./outputs/P1_INI-output.txt"

    # Reads text data from raw dataset as single-line array of characters
    with open(FILEPATHREAD, "r") as fr:
        data = str(fr.read())

    # Creates output file and writes appropriate response to file and notifies user
    with open(FILEPATHWRITE, "w") as fw:
        fw.write(" ".join(compute_DNA_nucleotide_counts(data)))

    return print("\nThe Nucleotide Counts dataset has been processed and the appropriate output has been saved to {}.\n".format(FILEPATHWRITE[2:]))

if __name__ == "__main__":
    main()