"""
NAME:               Computing GC Content (Bioinformatics Stronghold)
CONTRIBUTOR:        Aakash Sudhakar

PROBLEM:            The GC-content of a DNA string is given by the percentage of symbols in the string 
                    that are "C" or "G". For example, the GC-content of "AGCTATAG" is 37.5%. Note that the 
                    reverse complement of any DNA string has the same GC-content.

                    DNA strings must be labeled when they are consolidated into a database. A commonly used 
                    method of string labeling is called FASTA format. In this format, the string is introduced 
                    by a line that begins with ">", followed by some labeling information. Subsequent lines 
                    contain the string itself; the first line to begin with ">" indicates the label of 
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

STATUS:             Submission successful. 
"""

def select_best_gc_frequency(dna_gc_dict):
    """ Selects highest Rosalind DNA strand based on magnitude of 
    GC-content frequency in strand. """
    best_dna_strand, best_gc_content = None, 0
    # Iterates through DNA GC dictionary and selects highest GC-content value and matching strand
    for key, value in dna_gc_dict.items():
        if value > best_gc_content:
            best_dna_strand, best_gc_content = key, value
    return "{}\n{}".format(str(best_dna_strand), str(round(best_gc_content, 6)))

def gc_content_calculator(dna_strings):
    """ Calculates and returns dictogram from FASTA-formatted DNA strings 
    and sets as new value in returned dictionary. """
    gc_content, DNA_LENGTH = 0, len(dna_strings)
    # Iterates through DNA strings and quantifies GC content across strand
    for base in dna_strings:            
            if base == "G" or base == "C":
                gc_content += 1
    return float(100 * (gc_content / DNA_LENGTH))

def _parse_fasta_data(dataset):
    """ Parses FASTA data into dictionary with Rosalind keys defined as keys
    and DNA strings defined as values. """
    dna_dictionary, elements = dict(), dataset.strip().split(">")
    # Iterates through all strands and produces cleaned DNA dictionary of strands
    for el in elements:
        if len(el) == 0:
            continue
        parts = el.split()
        label, bases = parts[0], "".join(parts[1:])
        dna_dictionary[label] = bases
    return dna_dictionary

def main():
    """ Returns identified DNA string in FASTA format with relatively highest GC content frequency. """
    # NOTE: Requires being in parent repo ('pwd' must return up to directory '/Rosalind_Bioinformatics/Bioinformatics_Stronghold')
    FILEPATHREAD = "./datasets/P5_GC-dataset.txt"
    FILEPATHWRITE = "./outputs/P5_GC-output.txt"

    # Reads text data from raw dataset as single-line array of characters
    with open(FILEPATHREAD, "r") as fr:
        data = fr.read()
    
    # Functionally creates DNA GC content dictionary from raw data
    dna_gc_dict = dict([(key, gc_content_calculator(value)) for key, value in _parse_fasta_data(data).items()])

    # Creates output file and writes appropriate response to file and notifies user
    with open(FILEPATHWRITE, "w") as fw:
        fw.write(select_best_gc_frequency(dna_gc_dict))

    return print("\nThe GC-content dataset has been processed and the appropriate output has been saved to {}.\n".format(FILEPATHWRITE))

if __name__ == "__main__":
    main()