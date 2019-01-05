"""
NAME:               Introduction to Random Strings (Bioinformatics Stronghold)
CONTRIBUTOR:        Aakash Sudhakar

PROBLEM:            An array is a structure containing an ordered collection 
                    of objects (numbers, strings, other arrays, etc.). We let A[k] denote 
                    the k-th value in array A. You may like to think of an array as simply 
                    a matrix having only one row.

                    A random string is constructed so that the probability of choosing 
                    each subsequent symbol is based on a fixed underlying symbol frequency.

                    GC-content offers us natural symbol frequencies for constructing 
                    random DNA strings. If the GC-content is X, then we set the symbol 
                    frequencies of C and G equal to X/2 and the symbol frequencies 
                    of A and T equal to (1 − X)/2. For example, if the GC-content is 40%, 
                    then as we construct the string, the next symbol is 'G'/'C' with 
                    probability 0.2, and the next symbol is 'A'/'T' with probability 0.3.

                    In practice, many probabilities wind up being very small. In order to work 
                    with small probabilities, we may plug them into a function that "blows them up" 
                    for the sake of comparison. Specifically, the common logarithm of X 
                    (defined for X > 0 and denoted log10(X)) is the exponent to which we must 
                    raise 10 to obtain X.

DATASET:            A DNA string S of length at most 100 bp and an array A containing 
                    at most 20 numbers between 0 and 1.

OUTPUT:             An array B having the same length as A in which B[k] represents 
                    the common logarithm of the probability that a random string constructed 
                    with the GC-content found in A[k] will match S exactly.

SAMPLE DATASET:     ACGATACAA
                    0.129 0.287 0.423 0.476 0.641 0.742 0.783

SAMPLE OUTPUT:      -5.737 -5.217 -5.263 -5.360 -5.958 -6.628 -7.009

STATUS:             Pending.
"""

def main():
    # NOTE: Requires being in parent repo ('pwd' must return up to directory '/Rosalind_Bioinformatics/Bioinformatics_Stronghold')
    FILEPATHREAD = "./datasets/P28_PROB-sample.txt"
    # FILEPATHREAD = "./datasets/P28_PROB-dataset.txt"
    FILEPATHWRITE = "./outputs/P28_PROB-output.txt"

    # Reads text data from raw dataset
    with open(FILEPATHREAD, "r") as fr:
        data = fr.read()
    
    # Creates output file and writes appropriate response to file and notifies user
    with open(FILEPATHWRITE, "w") as fw:
        fw.write(str(data))

    return print("\nThe Random Strings dataset has been processed and the appropriate output has been saved to {}.\n".format(FILEPATHWRITE[2:]))

if __name__ == "__main__":
    main()