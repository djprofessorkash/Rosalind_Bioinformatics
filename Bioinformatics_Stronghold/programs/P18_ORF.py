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

def codon_translator(codon):
    """ Translates single codon using lookup table into effective amino acid. """
    amino_acid, CODON_TRANSLATION_TABLE = str(), {
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
    if len(codon) == 3:
        if codon in CODON_TRANSLATION_TABLE.keys():
            amino_acid = CODON_TRANSLATION_TABLE[codon]
    return amino_acid

def _produce_reverse_complement_strand(original_sequence):
    """ Produces reverse complement DNA sequence from original DNA sequence. """
    reverse_sequence, BASE_COMPLEMENT_TABLE = reversed(original_sequence), {
        "A": "U",
        "U": "A",
        "G": "C",
        "C": "G"
    }
    return "".join([BASE_COMPLEMENT_TABLE[base] for base in reverse_sequence])

def _discretize_unique_protein_sequences(protein_seq_for, protein_seq_rev):
    """ Discretizes DNA forward- and reverse-complement strands into combined protein chain list. """
    return "\n".join(set(protein_seq_for + protein_seq_rev))

def generate_all_protein_sequences(dna_sequence):
    """ Generates amino acid sequence from formatted codon sequence. """
    protein_sequences, codon_indices = list(), list()
    SEQ_SIZE = len(dna_sequence)
    # Initializes DNA sequence scanner for amino acid generation
    for iterator in range(SEQ_SIZE):
        amino_acid = codon_translator(dna_sequence[iterator:iterator+3])
        if amino_acid and amino_acid == "M":
            codon_indices.append(iterator)
    # Loops over DNA sequence and produces amino acid sequence
    for iterator in codon_indices:
        protein_sequence, stop_codon_found = str(), False
        for jterator in range(iterator, SEQ_SIZE, 3):
            amino_acid = codon_translator(dna_sequence[jterator:jterator+3])
            if not amino_acid:
                break
            if amino_acid == "Stop":
                stop_codon_found = True
                break
            protein_sequence += amino_acid
        if stop_codon_found:
            protein_sequences.append(protein_sequence)
    return protein_sequences

def main():
    # NOTE: Requires being in parent repo ('pwd' must return up to directory '/Rosalind_Bioinformatics/Bioinformatics_Stronghold')
    FILEPATHREAD = "./datasets/P18_ORF-dataset.txt"
    FILEPATHWRITE = "./outputs/P18_ORF-output.txt"

    # Reads text data from raw dataset as single-line array of characters
    with open(FILEPATHREAD, "r") as fr:
        data = "".join(line.strip() for line in fr.readlines()[1:]).replace("T", "U")

    protein_seq_for, protein_seq_rev = generate_all_protein_sequences(data), generate_all_protein_sequences(_produce_reverse_complement_strand(data))

    # Creates output file and writes appropriate response to file and notifies user
    with open(FILEPATHWRITE, "w") as fw:
        fw.write(_discretize_unique_protein_sequences(protein_seq_for, protein_seq_rev))

    return print("\nThe Open Reading Frames dataset has been processed and the appropriate output has been saved to {}.\n".format(FILEPATHWRITE[2:]))

if __name__ == "__main__":
    main()