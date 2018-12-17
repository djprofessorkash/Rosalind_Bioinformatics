"""
NAME:               Consensus and Profile (Bioinformatics Stronghold)
CONTRIBUTOR:        Aakash Sudhakar

PROBLEM:            A matrix is a rectangular table of values divided into 
                    rows and columns. An m × n matrix has m rows and n columns. 
                    Given a matrix A, we write A_{i,j} to indicate the value found 
                    at the intersection of row i and column j.

                    Say that we have a collection of DNA strings, all having 
                    the same length n. Their profile matrix is a 4 × n matrix P 
                    in which P_{1,j} represents the number of times that "A" occurs 
                    in the jth position of one of the strings, P_{2,j} represents the 
                    number of times that C occurs in the jth position, and so on (see below).

                    A consensus string c is a string of length n formed from 
                    our collection by taking the most common symbol at each position; 
                    the jth symbol of c therefore corresponds to the symbol having 
                    the maximum value in the j-th column of the profile matrix. 
                    Of course, there may be more than one most common symbol, 
                    leading to multiple possible consensus strings.

                                                A T C C A G C T
                                                G G G C A A C T
                                                A T G G A T C T
                            DNA Strings	        A A G C A A C C
                                                T T G G A A C T
                                                A T G C C A T T
                                                A T G G C A C T

                    	                    A   5 1 0 0 5 5 0 0
                            Profile	        C   0 0 1 4 2 0 6 1
                                            G   1 1 6 3 0 1 0 0
                                            T   1 5 0 0 0 1 1 6

                            Consensus	    A T G C A A C T


DATASET:            A collection of at most 10 DNA strings of equal length 
                    (at most 1 kbp) in FASTA format.

OUTPUT:             A consensus string and profile matrix for the collection. 
                    (If several possible consensus strings exist, then you may 
                    return any one of them.)

SAMPLE DATASET:     >Rosalind_1
                    ATCCAGCT
                    >Rosalind_2
                    GGGCAACT
                    >Rosalind_3
                    ATGGATCT
                    >Rosalind_4
                    AAGCAACC
                    >Rosalind_5
                    TTGGAACT
                    >Rosalind_6
                    ATGCCATT
                    >Rosalind_7
                    ATGGCACT

SAMPLE OUTPUT:      ATGCAACT
                    A: 5 1 0 0 5 5 0 0
                    C: 0 0 1 4 2 0 6 1
                    G: 1 1 6 3 0 1 0 0
                    T: 1 5 0 0 0 1 1 6

STATUS:             Submission successful. 
"""

# TODO: Implement class architecture around methods
# TODO: Optimize produce_consensus() and produce_profile() methods
def produce_consensus(profile):
    """ Returns parsed DNA consensus from DNA FASTA profile matrix. """
    dna_consensus = str()

    for base_freqs in list(zip(*profile.values())):
        if base_freqs[0] >= max(base_freqs[1], base_freqs[2], base_freqs[3]):
            dna_consensus += "A"
        elif base_freqs[1] >= max(base_freqs[0], base_freqs[2], base_freqs[3]):
            dna_consensus += "C"
        elif base_freqs[2] >= max(base_freqs[0], base_freqs[1], base_freqs[3]):
            dna_consensus += "G"
        elif base_freqs[3] >= max(base_freqs[0], base_freqs[1], base_freqs[2]):
            dna_consensus += "T"

    return dna_consensus

def produce_profile(dna_dict, n=8):
    """ Returns 4 x n profile matrix of counts of nitrogenous base occurrences
    from DNA FASTA dictionary. """
    dna_base_profile = {"A": [0] * n, 
                        "C": [0] * n, 
                        "G": [0] * n, 
                        "T": [0] * n}

    # Iterates through DNA bases and produces dictionary of frequencies per strand per base
    for key, value in dna_dict.items():
        for index in range(len(value)):
            dna_base_profile[value[index]][index] += 1

    return dna_base_profile

def parse_fasta_data(dataset):
    """ Parses FASTA data into dictionary with Rosalind keys defined as keys
    and DNA strings defined as values.\n
    Returns parsed FASTA data and general DNA strand length. """
    dna_dict, pairs = dict(), dataset.strip().split(">")

    # Iterates through all strands and produces cleaned DNA dictionary of strands and labels
    for pair in pairs:
        if len(pair) == 0:
            continue

        parts = pair.split()
        label, bases = parts[0], "".join(parts[1:])
        dna_dict[label] = bases
    
    values = list(dna_dict.values())

    # Verify integrity of FASTA DNA strand lengths and raise error if lengths are unequal
    for index in range(len(values) - 1):
        current_strand_length, next_strand_length = len(values[index]), len(values[index + 1])
        if current_strand_length != next_strand_length:
            raise ValueError("\n\nMISMATCH IN INPUT TEXT LENGTH FOUND: {} =/= {}. PLEASE VERIFY INTEGRITY OF FASTA DATA.\n".format(current_strand_length, next_strand_length))

    return dna_dict, current_strand_length

def main():
    # NOTE: Requires being in parent repo ('pwd' must return up to directory '/Rosalind_Bioinformatics/Bioinformatics_Stronghold')
    FILEPATHREAD = "./datasets/P10-sample.txt"
    FILEPATHWRITE = "./outputs/P10_CONS-output.txt"

    # Reads text data from raw dataset as single-line array of characters
    with open(FILEPATHREAD, "r") as fr:
        data = fr.read()

    # Produces profile and consensus based off of DNA base frequencies
    dna_dict, n = parse_fasta_data(data)
    profile = produce_profile(dna_dict, n)
    consensus = produce_consensus(profile)

    # Creates output file and writes appropriate response to file and notifies user
    with open(FILEPATHWRITE, "w") as fw:
        fw.write("{}\n".format(consensus))
        for base in profile:
            profile_data = " ".join([str(el) for el in profile[base]])
            fw.write("{}: {}\n".format(base, profile_data))

    return print("\nThe DNA Consensus dataset has been processed and the appropriate output has been saved to {}.\n".format(FILEPATHWRITE))
    

if __name__ == "__main__":
    main()