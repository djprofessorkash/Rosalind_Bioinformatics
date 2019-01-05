"""
NAME:               Transcribing DNA into RNA (Bioinformatics Stronghold)
CONTRIBUTOR:        Aakash Sudhakar

PROBLEM:            An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.
                    
                    Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed 
                    by replacing all occurrences of 'T' in t with 'U' in u.

DATASET:            A DNA string t having length at most 1000 nt.
OUTPUT:             The transcribed RNA string of t.

SAMPLE DATASET:     GATGGAACTTGACTACGTAAATT
SAMPLE OUTPUT:      GAUGGAACUUGACUACGUAAAUU

STATUS:             Submission successful. 
"""

def transcribe_DNA_into_RNA(nucleotide_collection):
    """ Transcribes DNA into RNA strand. """
    return "".join([[nucleotide, "U"][nucleotide == "T"] for nucleotide in nucleotide_collection])

def main():
    """ Returns new string with Ts converted to Us """
    # NOTE: Requires being in parent repo ('pwd' must return up to directory '/Rosalind_Bioinformatics/Bioinformatics_Stronghold')
    FILEPATHREAD = "./datasets/P2_RNA-dataset.txt"
    FILEPATHWRITE = "./outputs/P2_RNA-output.txt"

    # Reads text data from raw dataset as single-line array of characters
    with open(FILEPATHREAD, "r") as fr:
        original_strand = fr.read()

    # Creates output file and writes appropriate response to file and notifies user
    with open(FILEPATHWRITE, "w") as fw:
        fw.write("\n{}\n".format(transcribe_DNA_into_RNA(original_strand)))

    return print("\nThe RNA dataset has been processed and the appropriate output has been saved to {}.\n".format(FILEPATHWRITE))


if __name__ == "__main__":
    main()