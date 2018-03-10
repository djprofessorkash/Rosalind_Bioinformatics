"""
NAME:               Overlap Graphs (Bioinformatics Stronghold)
CONTRIBUTOR:        Aakash Sudhakar

PROBLEM:            A graph whose nodes have all been labeled can be represented 
                    by an adjacency list, in which each row of the list contains 
                    the two node labels corresponding to a unique edge.

                    A directed graph (or digraph) is a graph containing directed edges, 
                    each of which has an orientation. That is, a directed edge is 
                    represented by an arrow instead of a line segment; the starting 
                    and ending nodes of an edge form its tail and head, respectively. 
                    The directed edge with tail v and head w is represented by (v,w) 
                    (but not by (w,v)). A directed loop is a directed edge of the form (v,v).

                    For a collection of strings and a positive integer k, the overlap graph 
                    for the strings is a directed graph O_{k} in which each string is 
                    represented by a node, and string s is connected to string t with a 
                    directed edge when there is a length k suffix of s that matches 
                    a length k prefix of t, as long as s ≠ t; we demand s ≠ t to prevent 
                    directed loops in the overlap graph (although directed cycles may be 
                    present).

DATASET:            A collection of DNA strings in FASTA format having total length 
                    at most 10 kbp.

OUTPUT:             The adjacency list corresponding to O_{3}. 
                    You may return edges in any order.

SAMPLE DATASET:     >Rosalind_0498
                    AAATAAA
                    >Rosalind_2391
                    AAATTTT
                    >Rosalind_2323
                    TTTTCCC
                    >Rosalind_0442
                    AAATCCC
                    >Rosalind_5013
                    GGGTGGG

SAMPLE OUTPUT:      Rosalind_0498 Rosalind_2391
                    Rosalind_0498 Rosalind_0442
                    Rosalind_2391 Rosalind_2323

STATUS:             Pending.
"""

def main():
    # NOTE: Requires being in parent repo ('pwd' must return up to directory '/Rosalind_Bioinformatics/Bioinformatics_Stronghold')
    FILEPATHREAD = "./datasets/P12_sample.txt"
    # FILEPATHREAD = "./datasets/P12_GRPH-dataset.txt"
    FILEPATHWRITE = "./outputs/P12_GRPH-output.txt"

    # Reads text data from raw dataset as single-line array of characters
    with open(FILEPATHREAD, "r") as fr:
        data = fr.read()

    # Creates output file and writes appropriate response to file and notifies user
    with open(FILEPATHWRITE, "w") as fw:
        fw.write(str(data))

    return print("\nThe Overlap Graphs dataset has been processed and the appropriate output has been saved to {}.\n".format(FILEPATHWRITE[2:]))

if __name__ == "__main__":
    main()