"""
NAME:               RNA Splicing (Bioinformatics Stronghold)
CONTRIBUTOR:        Aakash Sudhakar

PROBLEM:            After identifying the exons and introns of an RNA string, we only need 
                    to delete the introns and concatenate the exons to form a new string 
                    ready for translation.

DATASET:            A DNA string s (of length at most 1 kbp) and a collection of substrings 
                    of s acting as introns. All strings are given in FASTA format.

OUTPUT:             A protein string resulting from transcribing and translating the exons 
                    of s. (Note: Only one solution will exist for the dataset provided.)

SAMPLE DATASET:     >Rosalind_10
                    ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
                    >Rosalind_12
                    ATCGGTCGAA
                    >Rosalind_15
                    ATCGGTCGAGCGTGT

SAMPLE OUTPUT:      MVYIADKQHVASREAYGHMFKVCA

STATUS:             Submission successful.
"""

# TODO: Improve function by making code more readable and efficient.
def _restructure_dataset(dataset, GENOME_LABELS):
    """ Restructures dataset into dictionary of main sequence and intron subsequences. """
    dataset_formatted, elements = dict(), dataset.strip().split(">")
    for index, element in enumerate(elements[1:]):
        components = element.split()
        current_sequence = "".join(components[1:])
        if index == 0:
            dataset_formatted[GENOME_LABELS[0]] = current_sequence
        else:
            if GENOME_LABELS[1] not in dataset_formatted:
                dataset_formatted[GENOME_LABELS[1]] = [current_sequence]
            else:
                dataset_formatted[GENOME_LABELS[1]].append(current_sequence)
    return dataset_formatted

# TODO: Improve function by conserving raw sequence without duplicating original data.
def genome_splicer(dataset):
    """ Detects introns across genomic sequence and splices them out. """
    GENOME_LABELS= ("sequence", "introns", "proteins")
    genomic_data = _restructure_dataset(dataset, GENOME_LABELS)
    for intron in genomic_data[GENOME_LABELS[1]]:
        if intron in genomic_data[GENOME_LABELS[0]]:
            genomic_data[GENOME_LABELS[0]] = genomic_data[GENOME_LABELS[0]].replace(intron, "")
    return genomic_data

def protein_constructor(sequence):
    """ Constructs protein chain from genomic data using amino acid lookup table. """
    protein_sequence, CODON_LENGTH, STOP_CODON = str(), 3, "Stop"
    for iterator in range(0, len(sequence), CODON_LENGTH):
        protein = _codon_translator(sequence[iterator:iterator+CODON_LENGTH].replace("T", "U"))
        if protein is STOP_CODON:
            break
        protein_sequence += protein
    return protein_sequence

def _codon_translator(codon):
    """ Translates single codon using lookup table into effective amino acid. """
    CODON_TRANSLATION_TABLE = {
        "UUU": "F",      "CUU": "L",      "AUU": "I",      "GUU": "V",
        "UUC": "F",      "CUC": "L",      "AUC": "I",      "GUC": "V",
        "UUA": "L",      "CUA": "L",      "AUA": "I",      "GUA": "V",
        "UUG": "L",      "CUG": "L",      "AUG": "M",      "GUG": "V",
        "UCU": "S",      "CCU": "P",      "ACU": "T",      "GCU": "A",
        "UCC": "S",      "CCC": "P",      "ACC": "T",      "GCC": "A",
        "UCA": "S",      "CCA": "P",      "ACA": "T",      "GCA": "A",
        "UCG": "S",      "CCG": "P",      "ACG": "T",      "GCG": "A",
        "UAU": "Y",      "CAU": "H",      "AAU": "N",      "GAU": "D",
        "UAC": "Y",      "CAC": "H",      "AAC": "N",      "GAC": "D",
        "UAA": "Stop",   "CAA": "Q",      "AAA": "K",      "GAA": "E",
        "UAG": "Stop",   "CAG": "Q",      "AAG": "K",      "GAG": "E",
        "UGU": "C",      "CGU": "R",      "AGU": "S",      "GGU": "G",
        "UGC": "C",      "CGC": "R",      "AGC": "S",      "GGC": "G",
        "UGA": "Stop",   "CGA": "R",      "AGA": "R",      "GGA": "G",
        "UGG": "W",      "CGG": "R",      "AGG": "R",      "GGG": "G"
    }
    if codon in CODON_TRANSLATION_TABLE.keys():
        return CODON_TRANSLATION_TABLE[codon]

def main():
    # NOTE: Requires being in parent repo ('pwd' must return up to directory '/Rosalind_Bioinformatics/Bioinformatics_Stronghold')
    FILEPATHREAD = "./datasets/P22_SPLC-dataset.txt"
    FILEPATHWRITE = "./outputs/P22_SPLC-output.txt"

    # Reads text data from raw dataset as single-line array of characters
    with open(FILEPATHREAD, "r") as fr:
        data = fr.read()
    
    # Creates output file and writes appropriate response to file and notifies user
    with open(FILEPATHWRITE, "w") as fw:
        fw.write(protein_constructor(genome_splicer(data)["sequence"]))

    return print("\nThe RNA Splicing dataset has been processed and the appropriate output has been saved to {}.\n".format(FILEPATHWRITE[2:]))

if __name__ == "__main__":
    main()