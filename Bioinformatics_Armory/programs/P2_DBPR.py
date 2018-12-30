"""
NAME:               Introduction to Protein Databases (Bioinformatics Armory)
CONTRIBUTOR:        Aakash Sudhakar

PROBLEM:            The UniProt Knowledgebase can be found at https://www.uniprot.org/help/uniprotkb.

                    You can see a complete description of a protein by entering 
                    its UniProt access ID into the site's query field. Equivalently, 
                    you may simply insert its ID (uniprot_id) directly into a UniProt hyperlink
                    as follows: http://www.uniprot.org/uniprot/uniprot_id.

                    For example, the data for protein B5ZC00 can be found 
                    at http://www.uniprot.org/uniprot/B5ZC00.

                    Swiss-Prot holds protein data as a structured .txt file. 
                    You can obtain it by simply adding .txt to the link:
                    http://www.uniprot.org/uniprot/uniprot_id.txt. 
                    
DATASET:            The UniProt ID of a protein.

OUTPUT:             A list of biological processes in which the protein 
                    is involved (biological processes are found in a subsection of 
                    the protein's "Gene Ontology" (GO) section).

SAMPLE DATASET:     Q5SLP9

SAMPLE OUTPUT:      DNA recombination
                    DNA repair
                    DNA replication

STATUS:             Pending.

PYTHON SHORTCUT:    ExPASy databases can be accessed automatically via 
                    Biopython’s Bio.ExPASy module. The function `.get_sprot_raw()` will find 
                    a target protein by its ID.

                    We can obtain data from an entry by using the SwissProt module. 
                    The `read()` function will handle one SwissProt record 
                    and `parse()` will allow you to read multiple records at a time.
"""

from Bio.Seq import Seq

def main():
    # NOTE: Requires being in parent repo ('pwd' must return up to directory '/Rosalind_Bioinformatics/Bioinformatics_Armory')
    FILEPATHREAD = "./datasets/P2_DBPR-sample.txt"
    # FILEPATHREAD = "./datasets/P2_DBPR-dataset.txt"
    FILEPATHWRITE = "./outputs/P2_DBPR-output.txt"

    # Reads text data from raw dataset
    with open(FILEPATHREAD, "r") as fr:
        data = str(fr.read())

    # Creates output file and writes appropriate response to file and notifies user
    with open(FILEPATHWRITE, "w") as fw:
        fw.write(str(data))

    return print("\nThe Protein Databases dataset has been processed and the appropriate output has been saved to {}.\n".format(FILEPATHWRITE[2:]))

if __name__ == "__main__":
    main()