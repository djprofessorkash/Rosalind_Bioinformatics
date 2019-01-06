"""
NAME:               Perfect Matchings and RNA Secondary Structures (Bioinformatics Stronghold)
CONTRIBUTOR:        Aakash Sudhakar

PROBLEM:            A matching in a graph G is a collection of edges of G for which no node 
                    belongs to more than one edge in the collection. If G contains an even 
                    number of nodes (say 2n), then a matching on G is perfect if it contains 
                    n edges, which is clearly the maximum possible.

                    First, let K_n denote the complete graph on 2n labeled nodes, in which 
                    every node is connected to every other node with an edge, and let p_n denote 
                    the total number of perfect matchings in K_n. For a given node X, there 
                    are 2n − 1 ways to join X to the other nodes in the graph, after which point 
                    we must form a perfect matching on the remaining 2n − 2 nodes. This reasoning 
                    provides us with the recurrence relation p_n = (2n − 1) * p_{n − 1}; 
                    using the fact that p_1 is 1, this recurrence relation implies 
                    the closed equation p_n = (2n − 1)(2n − 3)(2n − 5)...(3)(1).

                    Given an RNA string S = s_1, s_2, ..., s_n, a bonding graph for S is formed 
                    as follows. First, assign each symbol of S to a node, and arrange these nodes 
                    in order around a circle, connecting them with edges called adjacency edges. 
                    Second, form all possible edges {A, U} and {C, G}, called basepair edges; 
                    we will represent basepair edges with dashed edges.

                    Note that a matching contained in the basepair edges will represent 
                    one possibility for base pairing interactions in S. For such a matching 
                    to exist, S must have the same number of occurrences of 'A' as 'U' and 
                    the same number of occurrences of 'C' as 'G'.

DATASET:            An RNA string S of length at most 80 bp having the same number of occurrences 
                    of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.

OUTPUT:             The total possible number of perfect matchings of basepair edges 
                    in the bonding graph of S.

SAMPLE DATASET:     >Rosalind_23
                    AGCUAGUCAU

SAMPLE OUTPUT:      12

STATUS:             Submission failed.
"""

from math import factorial as fact

def calculate_perfect_matchings(sequence):
    """ Calculates perfect matchings of basepair edges across RNA input string. """
    gc_content, au_content = int(), int()
    for base in sequence:
        if base == "A":
            au_content += 1
        elif base == "G":
            gc_content += 1
    return fact(au_content) * fact(gc_content)

def main():
    # NOTE: Requires being in parent repo ('pwd' must return up to directory '/Rosalind_Bioinformatics/Bioinformatics_Stronghold')
    FILEPATHREAD = "./datasets/P26_PMCH-dataset.txt"
    FILEPATHWRITE = "./outputs/P26_PMCH-output.txt"

    # Reads text data from raw dataset
    with open(FILEPATHREAD, "r") as fr:
        data = "".join(fr.readlines()[1])
    
    return print(calculate_perfect_matchings(data))

    # Creates output file and writes appropriate response to file and notifies user
    with open(FILEPATHWRITE, "w") as fw:
        fw.write(str(calculate_perfect_matchings(data)))

    return print("\nThe Perfect Matchings dataset has been processed and the appropriate output has been saved to {}.\n".format(FILEPATHWRITE[2:]))

if __name__ == "__main__":
    main()