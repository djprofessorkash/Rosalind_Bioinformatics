"""
NAME:               Open Reading Frames (Bioinformatics Stronghold)
CONTRIBUTOR:        Aakash Sudhakar

PROBLEM:            Either strand of a DNA double helix can serve as the coding strand 
                    for RNA transcription. Hence, a given DNA string implies six total 
                    reading frames, or ways in which the same region of DNA can be 
                    translated into amino acids: three reading frames result from reading 
                    the string itself, whereas three more result from reading its reverse 
                    complement.

                    An open reading frame (ORF) is one which starts from the start codon 
                    and ends by stop codon, without any other stop codons in between. 
                    Thus, a candidate protein string is derived by translating an open 
                    reading frame into amino acids until a stop codon is reached.

DATASET:            A DNA string s of length at most 1 kbp in FASTA format.

OUTPUT:             Every distinct candidate protein string that can be translated from 
                    ORFs of s. Strings can be returned in any order.

SAMPLE DATASET:     >Rosalind_99
                    AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG

SAMPLE OUTPUT:      MLLGSFRLIPKETLIQVAGSSPCNLS
                    M
                    MGMTPRLGLESLLE
                    MTPRLGLESLLE

STATUS:             Pending.
"""

def main():
    # NOTE: Requires being in parent repo ('pwd' must return up to directory '/Rosalind_Bioinformatics/Bioinformatics_Stronghold')
    FILEPATHREAD = "./datasets/P18_sample.txt"
    # FILEPATHREAD = "./datasets/P18_ORF-dataset.txt"
    FILEPATHWRITE = "./outputs/P18_ORF-output.txt"

    # Reads text data from raw dataset as single-line array of characters
    with open(FILEPATHREAD, "r") as fr:
        data = fr.read()

    # Creates output file and writes appropriate response to file and notifies user
    with open(FILEPATHWRITE, "w") as fw:
        fw.write(str(data))

    return print("\nThe Open Reading Frames dataset has been processed and the appropriate output has been saved to {}.\n".format(FILEPATHWRITE[2:]))

if __name__ == "__main__":
    main()