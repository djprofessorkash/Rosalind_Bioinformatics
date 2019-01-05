"""
NAME:               Genome Assembly as Shortest Superstring (Bioinformatics Stronghold)
CONTRIBUTOR:        Aakash Sudhakar

PROBLEM:            For a collection of strings, a larger string containing every one 
                    of the smaller strings as a substring is called a superstring.

                    By the assumption of parsimony, a shortest possible superstring 
                    over a collection of reads serves as a candidate chromosome.

DATASET:            At most 50 DNA strings of approximately equal length, not exceeding 1 kbp, 
                    in FASTA format (which represent reads deriving from the same strand 
                    of a single linear chromosome).

                    The dataset is guaranteed to satisfy the following condition: there exists 
                    a unique way to reconstruct the entire chromosome from these reads by 
                    gluing together pairs of reads that overlap by more than half their length.

OUTPUT:             A shortest superstring containing all the given strings (thus corresponding 
                    to a reconstructed chromosome).

SAMPLE DATASET:     >Rosalind_56
                    ATTAGACCTG
                    >Rosalind_57
                    CCTGCCGGAA
                    >Rosalind_58
                    AGACCTGCCG
                    >Rosalind_59
                    GCCGGAATAC

SAMPLE OUTPUT:      ATTAGACCTGCCGGAATAC

STATUS:             Submission successful.
"""

def _parse_FASTA_data(dataset):
    """ Parses FASTA data into dictionary with Rosalind keys defined as keys
    and DNA strings defined as values. """
    substrings, elements = list(), dataset.strip().split(">")
    # Iterates through all strands and produces cleaned DNA dictionary of strands
    for el in elements:
        if len(el) == 0:
            continue
        parts = el.split()
        bases = "".join(parts[1:])
        substrings.append(bases)
    return substrings

# TODO: Improve function runtime by eliminating recursion depth on callstack
def construct_shortest_superstring(substrings, accumulator=""):
    """ Constructs shortest superstring synthesized from substring components. """
    if len(substrings) == 0:
        return accumulator
    elif len(accumulator) == 0:
        accumulator = substrings.pop(0)
        return construct_shortest_superstring(substrings, accumulator)
    else:
        for iterator in range(len(substrings)):
            substring = substrings[iterator]
            substring_size = len(substring)
            for jterator in range(round(substring_size / 2)):
                displacement = substring_size - jterator
                if accumulator.startswith(substring[jterator:]):
                    substrings.pop(iterator)
                    return construct_shortest_superstring(substrings, substring[:jterator] + accumulator)
                if accumulator.endswith(substring[:displacement]):
                    substrings.pop(iterator)
                    return construct_shortest_superstring(substrings, accumulator + substring[displacement:])

def main():
    # NOTE: Requires being in parent repo ('pwd' must return up to directory '/Rosalind_Bioinformatics/Bioinformatics_Stronghold')
    FILEPATHREAD = "./datasets/P25_LONG-dataset.txt"
    FILEPATHWRITE = "./outputs/P25_LONG-output.txt"

    # Reads text data from raw dataset
    with open(FILEPATHREAD, "r") as fr:
        data = fr.read()
    
    # Creates output file and writes appropriate response to file and notifies user
    with open(FILEPATHWRITE, "w") as fw:
        fw.write(str(construct_shortest_superstring(_parse_FASTA_data(data))))

    return print("\nThe Shortest Superstrings dataset has been processed and the appropriate output has been saved to {}.\n".format(FILEPATHWRITE[2:]))

if __name__ == "__main__":
    main()