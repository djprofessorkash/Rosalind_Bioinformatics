"""
NAME:               Computing GC Content (Bioinformatics Stronghold)
CONTRIBUTOR:        Aakash Sudhakar

PROBLEM:            The GC-content of a DNA string is given by the percentage of symbols in the string 
                    that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the 
                    reverse complement of any DNA string has the same GC-content.

                    DNA strings must be labeled when they are consolidated into a database. A commonly used 
                    method of string labeling is called FASTA format. In this format, the string is introduced 
                    by a line that begins with '>', followed by some labeling information. Subsequent lines 
                    contain the string itself; the first line to begin with '>' indicates the label of 
                    the next string.

                    In Rosalind's implementation, a string in FASTA format will be labeled by 
                    the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

DATASET:            At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
OUTPUT:             The ID of the string having the highest GC-content, followed by the GC-content 
                    of that string. Rosalind allows for a default error of 0.001 in all decimal answers 
                    unless otherwise stated.

SAMPLE DATASET:     >Rosalind_6404
                    CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
                    TCCCACTAATAATTCTGAGG

                    >Rosalind_5959
                    CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
                    ATATCCATTTGTCAGCAGACACGC

                    >Rosalind_0808
                    CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
                    TGGGAACCTGCGGGCAGTAGGTGGAAT
                    
SAMPLE OUTPUT:      Rosalind_0808
                    60.919540

STATUS:             Incomplete.
"""


def main():
    """ ... """

if __name__ == "__main__":
    main()