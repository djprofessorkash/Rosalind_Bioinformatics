"""
NAME:               Longest Increasing Subsequence (Bioinformatics Stronghold)
CONTRIBUTOR:        Aakash Sudhakar

PROBLEM:            A subsequence of a permutation is a collection of elements of 
                    the permutation in the order that they appear. For example, 
                    (5, 3, 4) is a subsequence of (5, 1, 3, 4, 2).

                    A subsequence is increasing if the elements of the subsequence increase, 
                    and decreasing if the elements decrease. For example, given 
                    the permutation (8, 2, 1, 6, 5, 7, 4, 3, 9), an increasing subsequence 
                    is (2, 6, 7, 9), and a decreasing subsequence is (8, 6, 5, 4, 3). 
                    You may verify that these two subsequences are as long as possible.

DATASET:            A positive integer n ≤ 10000 followed by a permutation π of length n.

OUTPUT:             A longest increasing subsequence of π, followed by a 
                    longest decreasing subsequence of π.

SAMPLE DATASET:     5
                    5 1 4 2 3

SAMPLE OUTPUT:      1 2 3
                    5 4 2

STATUS:             Submission successful.
"""

# TODO: Improve function runtime (double-loop)
def determine_longest_subsequence(sequence, order):
    """ Determines longest subsequence from input sequence permutation. """
    subsequences = [0] * len(sequence)
    for iterator in range(len(sequence) - 2, -1, -1):
        for jterator in range(len(sequence) - 1, iterator, -1):
            if order == "INCREASING":
                if sequence[iterator] < sequence[jterator] and subsequences[iterator] <= subsequences[jterator]:
                    subsequences[iterator] += 1
            if order == "DECREASING":
                if sequence[iterator] > sequence[jterator] and subsequences[iterator] <= subsequences[jterator]:
                    subsequences[iterator] = subsequences[jterator] + 1
    maximum_subsequence, longest_subsequence = max(subsequences), list()
    for iterator in range(len(subsequences)):
        if maximum_subsequence == subsequences[iterator]:
            longest_subsequence.append(str(sequence[iterator]))
            maximum_subsequence -= 1
    return longest_subsequence

def main():
    # NOTE: Requires being in parent repo ('pwd' must return up to directory '/Rosalind_Bioinformatics/Bioinformatics_Stronghold')
    FILEPATHREAD = "./datasets/P24_LGIS-dataset.txt"
    FILEPATHWRITE = "./outputs/P24_LGIS-output.txt"

    # Reads text data from raw dataset
    with open(FILEPATHREAD, "r") as fr:
        π = [int(item) for item in fr.readlines()[1].split(" ")]

    longest_subsequences = dict()
    for order in ("INCREASING", "DECREASING"):
        longest_subsequences["LONGEST_{}_SUBSEQUENCE".format(order)] = determine_longest_subsequence(π, order)

    # Creates output file and writes appropriate response to file and notifies user
    with open(FILEPATHWRITE, "w") as fw:
        fw.write("\n".join([" ".join(longest_subsequences["LONGEST_{}_SUBSEQUENCE".format(order)]) for order in ("INCREASING", "DECREASING")]))

    return print("\nThe Increasing Subsequences dataset has been processed and the appropriate output has been saved to {}.\n".format(FILEPATHWRITE[2:]))

if __name__ == "__main__":
    main()