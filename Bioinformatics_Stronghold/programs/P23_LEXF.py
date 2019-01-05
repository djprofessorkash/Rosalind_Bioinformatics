"""
NAME:               Enumerating k-mers Lexicographically (Bioinformatics Stronghold)
CONTRIBUTOR:        Aakash Sudhakar

PROBLEM:            Assume that an alphabet 𝒜 has a predetermined order; that is, we write 
                    the alphabet as a permutation 𝒜 = (a_1, a_2, ..., a_k), 
                    where a_1 < a_2 < ... < a_k. For instance, the English alphabet 
                    is organized as (A, B, ..., Z).

                    Given two strings s and t having the same length n, we say that 
                    s precedes t in the lexicographic order (and write s < Lex(t)) if the 
                    first symbol s[j] that doesn't match t[j] satisfies s_j < t_j in 𝒜.

DATASET:            A collection of at most 10 symbols defining an ordered alphabet, and 
                    a positive integer n (n ≤ 10).

OUTPUT:             All strings of length n that can be formed from the alphabet, ordered 
                    lexicographically (use the standard order of symbols in the English alphabet).

SAMPLE DATASET:     A C G T
                    2

SAMPLE OUTPUT:      AA
                    AC
                    AG
                    AT
                    CA
                    CC
                    CG
                    CT
                    GA
                    GC
                    GG
                    GT
                    TA
                    TC
                    TG
                    TT

STATUS:             Submission successful.
"""

from itertools import product

def _grab_relevant_data(dataset):
    """ Grabs relevant symbols and permutative constant for future lexicographic generation. """
    return sorted(list(dataset[0].strip().split(" "))), int(dataset[1])

# TODO: Improve function by creating custom itertools.product() data structure
def generate_ordered_lexicograph(symbol_collection, N):
    """ Generates lexicographically ordered sequence of symbol permutations based on input parameters. """
    return ["".join(item) for item in product(symbol_collection, repeat=N)]

def main():
    # NOTE: Requires being in parent repo ('pwd' must return up to directory '/Rosalind_Bioinformatics/Bioinformatics_Stronghold')
    FILEPATHREAD = "./datasets/P23_LEXF-dataset.txt"
    FILEPATHWRITE = "./outputs/P23_LEXF-output.txt"

    # Reads text data from raw dataset
    with open(FILEPATHREAD, "r") as fr:
        symbols, N = _grab_relevant_data(fr.readlines())
    
    # Creates output file and writes appropriate response to file and notifies user
    with open(FILEPATHWRITE, "w") as fw:
        fw.write("\n".join(generate_ordered_lexicograph(symbols, N)))

    return print("\nThe Lexicographic Sorting dataset has been processed and the appropriate output has been saved to {}.\n".format(FILEPATHWRITE[2:]))

if __name__ == "__main__":
    main()