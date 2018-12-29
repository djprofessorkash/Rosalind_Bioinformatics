"""
NAME:               Independent Alleles (Bioinformatics Stronghold)
CONTRIBUTOR:        Aakash Sudhakar

PROBLEM:            Two events A and B are independent if Pr(A and B) is equal to 
                    Pr(A) × Pr(B). In other words, the events do not influence each other, 
                    so that we may simply calculate each of the individual probabilities 
                    separately and then multiply.

                    More generally, random variables X and Y are independent if whenever 
                    A and B are respective events for X and Y, A and B are independent 
                    (i.e., Pr(A and B) = Pr(A) × Pr(B)).

                    As an example of how helpful independence can be for calculating 
                    probabilities, let X and Y represent the numbers showing on 
                    two six-sided dice. Intuitively, the number of pips showing on one die 
                    should not affect the number showing on the other die. If we want to 
                    find the probability that X + Y is odd, then we don't need to draw a tree 
                    diagram and consider all possibilities. We simply first note that for 
                    X + Y to be odd, either X is even and Y is odd or X is odd and Y is even. 
                    
                    In terms of probability:  
                    Pr(X + Y is odd) = Pr(X is even and Y is odd) + Pr(X is odd and Y is even).

                    Using independence, this becomes: 
                    [Pr(X is even) × Pr(Y is odd)] + [Pr(X is odd) × Pr(Y is even)], 
                    or [(1/2) × 2] + [(1/2) × 2] = 1/2. 

DATASET:            Two positive integers k (k ≤ 7) and N (N ≤ 2^k). In this problem, 
                    we begin with Tom, who in the 0th generation has genotype Aa Bb. 
                    Tom has two children in the 1st generation, each of whom has 
                    two children, and so on. Each organism always mates with an organism 
                    having genotype Aa Bb.

OUTPUT:             The probability that at least N Aa Bb organisms will belong to the 
                    k-th generation of Tom's family tree (don't count the Aa Bb mates 
                    at each level). Assume that Mendel's second law holds for the factors.

SAMPLE DATASET:     2 1
SAMPLE OUTPUT:      0.684

STATUS:             Submission successful.
"""

from math import factorial as fact

def determine_binomial_distributive_probability(k, N):
    """ Calculates cumulative probability across binomial distribution of allelic occurrences. """
    trials, proba_final = 2**k, int()       # Ascertains total number of trials/allelic occurrences
    for iterator in range(N, trials + 1):
        # Calculates the binomial coefficient and main expressions of the binomial equation
        binomial_coeff = fact(trials) / (fact(iterator) * fact(trials - iterator))
        p, q = 0.25 ** iterator, 0.75 ** (trials - iterator)

        # Sums the relative probability across each iteration
        proba_final += binomial_coeff * p * q
    return round(proba_final, 3)

def main():
    # NOTE: Requires being in parent repo ('pwd' must return up to directory '/Rosalind_Bioinformatics/Bioinformatics_Stronghold')
    FILEPATHREAD = "./datasets/P15_LIA-dataset.txt"
    FILEPATHWRITE = "./outputs/P15_LIA-output.txt"

    # Reads text data from raw dataset as single-line array of characters
    with open(FILEPATHREAD, "r") as fr:
        k, N = [int(value) for value in fr.read().strip().split(" ")]

    # Creates output file and writes appropriate response to file and notifies user
    with open(FILEPATHWRITE, "w") as fw:
        fw.write(str(determine_binomial_distributive_probability(k, N)))

    return print("\nThe Independent Alleles dataset has been processed and the appropriate output has been saved to {}.\n".format(FILEPATHWRITE[2:]))

if __name__ == "__main__":
    main()