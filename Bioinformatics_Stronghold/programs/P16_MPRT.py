"""
NAME:               Finding a Protein Motif (Bioinformatics Stronghold)
CONTRIBUTOR:        Aakash Sudhakar

PROBLEM:            To allow for the presence of its varying forms, a protein motif 
                    is represented by a shorthand as follows: [XY] means "either X or Y" 
                    and {X} means "any amino acid except X." For example, 
                    the N-glycosylation motif is written as N{P}[ST]{P}.

                    You can see the complete description and features of a particular 
                    protein by its access ID "uniprot_id" in the UniProt database, 
                    by inserting the ID number into http://www.uniprot.org/uniprot/uniprot_id.

                    Alternatively, you can obtain a protein sequence in FASTA format 
                    by following http://www.uniprot.org/uniprot/uniprot_id.fasta.

                    For example, the data for protein B5ZC00 can be found at 
                    http://www.uniprot.org/uniprot/B5ZC00.

                    NOTE: Some entries in UniProt have one primary (citable) accession number 
                    and some secondary numbers, appearing due to merging or demerging entries. 
                    In this problem, you may be given any type of ID. If you type the 
                    secondary ID into the UniProt query, then you will be automatically 
                    redirected to the page containing the primary ID. 
                    
DATASET:            At most 15 UniProt Protein Database access IDs.

OUTPUT:             For each protein possessing the N-glycosylation motif, output its 
                    given access ID followed by a list of locations in the protein string 
                    where the motif can be found.

SAMPLE DATASET:     A2Z669
                    B5ZC00
                    P07204_TRBM_HUMAN
                    P20840_SAG1_YEAST

SAMPLE OUTPUT:      B5ZC00
                    85 118 142 306 395
                    P07204_TRBM_HUMAN
                    47 115 116 382 409
                    P20840_SAG1_YEAST
                    79 109 135 248 306 348 364 402 485 501 614

STATUS:             Pending.
"""

def main():
    # NOTE: Requires being in parent repo ('pwd' must return up to directory '/Rosalind_Bioinformatics/Bioinformatics_Stronghold')
    FILEPATHREAD = "./datasets/P16_sample.txt"
    # FILEPATHREAD = "./datasets/P16_MPRT-dataset.txt"
    FILEPATHWRITE = "./outputs/P16_MPRT-output.txt"

    # Reads text data from raw dataset as single-line array of characters
    with open(FILEPATHREAD, "r") as fr:
        data = fr.read()

    # Creates output file and writes appropriate response to file and notifies user
    with open(FILEPATHWRITE, "w") as fw:
        fw.write(str(data))

    return print("\nThe Protein Motifs dataset has been processed and the appropriate output has been saved to {}.\n".format(FILEPATHWRITE[2:]))

if __name__ == "__main__":
    main()