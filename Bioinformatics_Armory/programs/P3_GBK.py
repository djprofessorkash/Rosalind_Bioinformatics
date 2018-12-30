"""
NAME:               GenBank Introduction (Bioinformatics Armory)
CONTRIBUTOR:        Aakash Sudhakar

PROBLEM:            GenBank comprises several subdivisions:
                        - Nucleotide: a collection of nucleic acid sequences from several sources.
                            (https://www.ncbi.nlm.nih.gov/nucleotide)
                        - Genome Survey Sequence (GSS): uncharacterized short genomic sequences.
                            (https://www.ncbi.nlm.nih.gov/gss)
                        - Expressed Sequence Tags (EST): uncharacterized short cDNA sequences. 
                            (https://www.ncbi.nlm.nih.gov/est)

                    Searching the Nucleotide database with general text queries will produce 
                    the most relevant results. You can also use a simple query based on 
                    protein name, gene name or gene symbol.

                    To limit your search to only certain kinds of records, you can search 
                    using GenBank's Limits page or alternatively use the Filter your 
                    results field to select categories of records after a search.

                    If you cannot find what you are searching for, check how the database 
                    interpreted your query by investigating the Search details field on the 
                    right side of the page. This field automatically translates your search 
                    into standard keywords.

                    For example, if you search for Drosophila, the Search details field will 
                    contain (Drosophila[All Fields]), and you will obtain all entries 
                    that mention Drosophila (including all its endosymbionts). You can 
                    restrict your search to only organisms belonging to the Drosophila genus 
                    by using a search tag and searching for Drosophila[Organism].
                    
DATASET:            A genus name, followed by two dates in YYYY/M/D format.

OUTPUT:             The number of Nucleotide GenBank entries for the given genus 
                    that were published between the dates specified.

SAMPLE DATASET:     Anthoxanthum
                    2003/7/25
                    2005/12/27

SAMPLE OUTPUT:      7

STATUS:             Pending.

PYTHON SHORTCUT:    NCBI's databases, such as PubMed, GenBank, GEO, and many others, 
                    can be accessed via Entrez, a data retrieval system offered by NCBI. 
                    For direct access to Entrez, you can use Biopython’s Bio.Entrez module.

                    The Bio.Entrez.esearch() function will search any of the NCBI databases. 
                    This function takes the following arguments:
                        - db: The database to search. For example, this field can be 
                            nucleotide for GenBank or pubmed for PubMed.
                        - term: The search term for the "Query" field. You can use 
                            search tags here.
                    
                    NOTE: When you request Entrez databases you must obey NCBI's requirements:
                        - For any series of more than 100 requests, access the database on 
                            the weekend or outside peak times in the US.
                        - Make no more than three requests every second.
                        - Fill in the Entrez.email field so that NCBI can contact you if 
                            there is a problem.
                        - Be sensible with your usage levels; if you want to download 
                            whole mammalian genomes, use NCBI's FTP.
"""

from Bio.Seq import Seq

def main():
    # NOTE: Requires being in parent repo ('pwd' must return up to directory '/Rosalind_Bioinformatics/Bioinformatics_Armory')
    FILEPATHREAD = "./datasets/P3_GBK-sample.txt"
    # FILEPATHREAD = "./datasets/P3_GBK-dataset.txt"
    FILEPATHWRITE = "./outputs/P3_GBK-output.txt"

    # Reads text data from raw dataset
    with open(FILEPATHREAD, "r") as fr:
        data = str(fr.read())

    # Creates output file and writes appropriate response to file and notifies user
    with open(FILEPATHWRITE, "w") as fw:
        fw.write(str(data))

    return print("\nThe GenBank dataset has been processed and the appropriate output has been saved to {}.\n".format(FILEPATHWRITE[2:]))

if __name__ == "__main__":
    main()