"""
NAME:               Finding a Motif in DNA (Bioinformatics Stronghold)
CONTRIBUTOR:        Aakash Sudhakar

PROBLEM:            Given two strings s and t, t is a substring of s if 
                    t is contained as a contiguous collection of symbols in s 
                    (as a result, t must be no longer than s).

                    The position of a symbol in a string is the total 
                    number of symbols found to its left, including itself 
                    (e.g., the positions of all occurrences of 'U' in 
                    "AUGCUUCAGAAAGGUCUUACG" are 2, 5, 6, 15, 17, and 18). 
                    The symbol at position i of s is denoted by s[i].

                    A substring of s can be represented as s[j:k], 
                    where j and k represent the starting and 
                    ending positions of the substring in s; for example, 
                    if s = "AUGCUUCAGAAAGGUCUUACG", then s[2:5] = "UGCU".

                    The location of a substring s[j:k] is its beginning position j; 
                    note that t will have multiple locations in s if it occurs 
                    more than once as a substring of s.

DATASET:            Two DNA strings s and t (each of length at most 1 kbp).

OUTPUT:             All locations of t as a substring of s.

SAMPLE DATASET:     GATATATGCATATACTT
                    ATAT
SAMPLE OUTPUT:      2 4 10

STATUS:             Submission successful.
"""

def substring_match(s, t):
    """ Returns stringified list of found indices where pattern exists in text
    or returns None if no found indices. """
    # Creates list of found indices where target pattern has been located in input text
    found_indices = [str(index + 1) for index in range(len(s)) if s.find(t, index) == index]
    # Returns joined string of found indices if list has at least one found index
    if len(found_indices) >= 1:
        return " ".join(found_indices)
    return None

def main():
    # NOTE: Requires being in parent repo ('pwd' must return up to directory '/Rosalind_Bioinformatics/Bioinformatics_Stronghold')
    FILEPATHREAD = "./datasets/P9_SUBS-dataset.txt"
    FILEPATHWRITE = "./outputs/P9_SUBS-output.txt"

    # Reads text data from raw dataset as single-line array of characters
    with open(FILEPATHREAD, "r") as fr:
        data = str(fr.readlines())

    text, pattern = data[0].strip(), data[1].strip()

    # Creates output file and writes appropriate response to file and notifies user
    with open(FILEPATHWRITE, "w") as fw:
        fw.write(str(substring_match(text, pattern)))

    return print("\nThe DNA Substrings dataset has been processed and the appropriate output has been saved to {}.\n".format(FILEPATHWRITE))

if __name__ == "__main__":
    main()