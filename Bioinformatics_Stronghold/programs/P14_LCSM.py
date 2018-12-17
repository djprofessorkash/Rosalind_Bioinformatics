"""
NAME:               Finding a Shared Motif (Bioinformatics Stronghold)
CONTRIBUTOR:        Aakash Sudhakar

PROBLEM:            A common substring of a collection of strings is a substring of 
                    every member of the collection. We say that a common substring is 
                    a longest common substring if there does not exist a longer 
                    common substring. For example, "CG" is a common substring of "ACGTACGT" 
                    and "AACCGTATA", but it is not as long as possible; in this case, 
                    "CGTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".

                    Note that the longest common substring is not necessarily unique; 
                    for a simple example, "AA" and "CC" are both longest common substrings 
                    of "AACC" and "CCAA".

DATASET:            A collection of k (k≤100) DNA strings of length at most 1 kbp each 
                    in FASTA format.

OUTPUT:             A longest common substring of the collection. 
                    (If multiple solutions exist, you may return any single solution.)

SAMPLE DATASET:     >Rosalind_1
                    GATTACA
                    >Rosalind_2
                    TAGACCA
                    >Rosalind_3
                    ATACA

SAMPLE OUTPUT:      AC

STATUS:             Submission failed: INCORRECT.
"""

def _parse_fasta_data(dataset):
    """ Helper function to parse FASTA data into useful form. """
    parsed_data = list()
    for count, line in enumerate(dataset, start=1):
        if count % 2 == 0:
            parsed_data.append(line.strip())
    return parsed_data

def sequence_extractor(parsed_data):
    """ Function to extract common subsequence among all FASTA data into shared motif. """
    shared_motif = str()

    # Isolates shortest sequence for parametrically faster subsequence search
    sorted_sequences = sorted(parsed_data, key=len)
    comparator_sequence, accessory_sequences = sorted_sequences[0], sorted_sequences[1:]

    # Double loop to comparatively identify shortest subsequence match among all sequences
    for outer_iterator in range(len(comparator_sequence)):
        for inner_iterator in range(outer_iterator, len(comparator_sequence)):
            subsequence, is_found = comparator_sequence[outer_iterator:inner_iterator + 1], False

            # Flag manipulation to identify continuous character matches in subsequence
            for sequence in accessory_sequences:
                if subsequence in sequence:
                    is_found = True
                else:
                    is_found = False
                    break

            # Longest common subsequence is set to shared motif variable
            if is_found and len(subsequence) > len(shared_motif):
                shared_motif = subsequence
    return shared_motif

def main():
    # NOTE: Requires being in parent repo ('pwd' must return up to directory '/Rosalind_Bioinformatics/Bioinformatics_Stronghold')
    # FILEPATHREAD = "./datasets/P14_LCSM-sample.txt"
    FILEPATHREAD = "./datasets/P14_LCSM-dataset.txt"
    FILEPATHWRITE = "./outputs/P14_LCSM-output.txt"

    # Reads text data from raw dataset as single-line array of characters
    with open(FILEPATHREAD, "r") as fr:
        data = fr.readlines()

    # Creates output file and writes appropriate response to file and notifies user
    with open(FILEPATHWRITE, "w") as fw:
        fw.write(sequence_extractor(_parse_fasta_data(data)))

    return print("\nThe Shared Motif dataset has been processed and the appropriate output has been saved to {}.\n".format(FILEPATHWRITE[2:]))

if __name__ == "__main__":
    main()