"""
NAME:               Locating Restriction Sites (Bioinformatics Stronghold)
CONTRIBUTOR:        Aakash Sudhakar

PROBLEM:            A DNA string is a reverse palindrome if it is equal to its 
                    reverse complement. For instance, GCATGC is a reverse palindrome 
                    because its reverse complement is GCATGC. 

DATASET:            A DNA string of length at most 1 kbp in FASTA format.

OUTPUT:             The position and length of every reverse palindrome in the string 
                    having length between 4 and 12. You may return these pairs in any order.

SAMPLE DATASET:     >Rosalind_24
                    TCAATGCATGCGGGTCTATATGCAT

SAMPLE OUTPUT:      4 6
                    5 4
                    6 6
                    7 4
                    17 4
                    18 4
                    20 6
                    21 4

STATUS:             Submission successful.

NOTE:               Shoutout to Rohan Mishra for his masterful algorithmic debugging help. 
"""

def produce_complement_strands(subsequence):
    """ Produces pair of original and reverse complement DNA strands. """
    reverse_sequence, BASE_COMPLEMENT_TABLE = reversed(subsequence), {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }
    return "".join([BASE_COMPLEMENT_TABLE[base] for base in reverse_sequence])

def _is_reverse_palindrome(subsequence):
    """ Checks if input DNA subsequence is reverse palindrome. """
    return subsequence == produce_complement_strands(subsequence)

# TODO: Fix function so it can detect multiple restriction sites at same position
def locate_restriction_sites(original_sequence):
    """ Locates restriction site positions and lengths of reverse palindromes across paired complements. """
    restrictions_sites, sequence_size = list(), len(original_sequence)
    LOCAL_MIN, LOCAL_MAX = 4, 13
    for iterator in range(sequence_size):
        for jterator in range(LOCAL_MIN, LOCAL_MAX):
            if iterator + jterator > sequence_size:
                continue
            subsequence = original_sequence[iterator:iterator+jterator]
            if _is_reverse_palindrome(subsequence):
                restrictions_sites.append((iterator + 1, jterator))
    return restrictions_sites

def main():
    # NOTE: Requires being in parent repo ('pwd' must return up to directory '/Rosalind_Bioinformatics/Bioinformatics_Stronghold')
    FILEPATHREAD = "./datasets/P21_REVP-dataset.txt"
    FILEPATHWRITE = "./outputs/P21_REVP-output.txt"

    # Reads text data from raw dataset as single-line array of characters
    with open(FILEPATHREAD, "r") as fr:
        data = str("".join(line.strip() for line in fr.readlines()[1:]))

    # Computes restriction sites across DNA sequence using reverse complement determination
    restriction_sites = locate_restriction_sites(data)

    # Creates output file and writes appropriate response to file and notifies user
    with open(FILEPATHWRITE, "w") as fw:
        fw.write("\n".join([" ".join(map(str, item)) for item in restriction_sites]))

    return print("\nThe Restriction Sites dataset has been processed and the appropriate output has been saved to {}.\n".format(FILEPATHWRITE[2:]))

if __name__ == "__main__":
    main()