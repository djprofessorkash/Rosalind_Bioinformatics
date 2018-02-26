"""
NAME:               Mendel's First Law (Bioinformatics Stronghold)
CONTRIBUTOR:        Aakash Sudhakar

PROBLEM:            Probability is the mathematical study of randomly occurring phenomena. 
                    We will model such a phenomenon with a random variable, which is simply a 
                    variable that can take a number of different distinct outcomes depending on 
                    the result of an underlying random process.

                    For example, say that we have a bag containing 3 red balls and 2 blue balls. 
                    If we let X represent the random variable corresponding to the color of 
                    a drawn ball, then the probability of each of the two outcomes is given by 
                    Pr(X = red) = 3/5 and Pr(X = blue) = 2/5.

                    Random variables can be combined to yield new random variables. Returning to 
                    the ball example, let Y model the color of a second ball drawn from 
                    the bag (without replacing the first ball). The probability of Y being red 
                    depends on whether the first ball was red or blue. To represent all outcomes 
                    of X and Y, we therefore use a probability tree diagram. This branching diagram 
                    represents all possible individual probabilities for X and Y, with outcomes 
                    at the endpoints ("leaves") of the tree. The probability of any outcome 
                    is given by the product of probabilities along the path from the beginning 
                    of the tree.

                    An event is simply a collection of outcomes. Because outcomes are distinct, 
                    the probability of an event can be written as the sum of the probabilities of 
                    its constituent outcomes. For our colored ball example, let A be 
                    the event "Y is blue." Pr(A) is equal to the sum of the probabilities of 
                    two different outcomes: Pr(X = blue & Y = blue) + Pr(X = red & Y = blue),
                    or 3/10 + 1/10 = 2/5.

                    HINT:   Consider simulating inheritance on a number of small test cases 
                            in order to check your solution.

DATASET:            Three positive integers k, m, and n, representing a population containing 
                    k + m + n organisms: k individuals are homozygous dominant for a factor, 
                    m are heterozygous, and n are homozygous recessive.

OUTPUT:             The probability that two randomly selected mating organisms will produce 
                    an individual possessing a dominant allele (and thus displaying 
                    the dominant phenotype). Assume that any two organisms can mate.

SAMPLE DATASET:     2 2 2
SAMPLE OUTPUT:      0.78333

STATUS:             Incomplete.
"""


def main():
    # NOTE: Requires being in parent repo ('pwd' must return up to directory '/Rosalind_Bioinformatics/Bioinformatics_Stronghold')
    FILEPATHREAD = "./datasets/P7_IPRB-dataset.txt"
    FILEPATHWRITE = "./outputs/P7_IPRB-output.txt"

    # Reads text data from raw dataset as single-line array of characters
    with open(FILEPATHREAD, "r") as fr:
        data = fr.read().split(" ")
    k, m, n = data[0], data[1], data[2]

    # Creates output file and writes appropriate response to file and notifies user
    with open(FILEPATHWRITE, "w") as fw:
        fw.write()

    return print("\nThe Mendelian Probability dataset has been processed and the appropriate output has been saved to {}.\n".format(FILEPATHWRITE))

if __name__ == "__main__":
    main()