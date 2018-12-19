"""
NAME:               Calculating Expected Offspring (Bioinformatics Stronghold)
CONTRIBUTOR:        Aakash Sudhakar

PROBLEM:            For a random variable X taking integer values between 1 and n, 
                    the expected value of X is E(X) = {n}∑{k = 1}(k × Pr(X = k)). 
                    The expected value offers us a way of taking the long-term average 
                    of a random variable over a large number of trials.

                    As a motivating example, let X be the number on a six-sided die. 
                    Over a large number of rolls, we should expect to obtain an average 
                    of 3.5 on the die (even though it's not possible to roll a 3.5). 
                    The formula for expected value confirms that 
                    E(X) = {6}∑{k = 1}(k × Pr(X = k)) = 3.5.

                    More generally, a random variable for which every one of a number 
                    of equally spaced outcomes has the same probability is called a 
                    uniform random variable (in the die example, this "equal spacing" 
                    is equal to 1). We can generalize our die example to find that if X 
                    is a uniform random variable with minimum possible value a and 
                    maximum possible value b, then E(X) = (a + b)/2. You may also wish to 
                    verify that for the dice example, if Y is the random variable 
                    associated with the outcome of a second die roll, then E(X + Y) = 7.

DATASET:            Six nonnegative integers, each of which does not exceed 20,000. 
                    The integers correspond to the number of couples in a population 
                    possessing each genotype pairing for a given factor. 
                    In order, the six given integers represent the number of couples 
                    having the following genotypes:

                                            1. AA-AA
                                            2. AA-Aa
                                            3. AA-aa
                                            4. Aa-Aa
                                            5. Aa-aa
                                            6. aa-aa

OUTPUT:             The expected number of offspring displaying the dominant phenotype 
                    in the next generation, under the assumption that every couple 
                    has exactly two offspring.

SAMPLE DATASET:     1 0 0 1 0 1
SAMPLE OUTPUT:      3.5

STATUS:             Submission successful.
"""

def expected_value_calculator(dataset):
    """ Function to calculate total expected dominant values from data. """
    dominant_genotype_table, expected_value = [1.0, 1.0, 1.0, 0.75, 0.5, 0], 0
    
    # Static loop that aggregates dominant gene occurrences from data and data-table
    for number in range(6):
        expected_value += 2 * dataset[number] * dominant_genotype_table[number] 
    return expected_value

def main():
    # NOTE: Requires being in parent repo ('pwd' must return up to directory '/Rosalind_Bioinformatics/Bioinformatics_Stronghold')
    FILEPATHREAD = "./datasets/P13_IEV-dataset.txt"
    FILEPATHWRITE = "./outputs/P13_IEV-output.txt"

    # Reads text data from raw dataset as single-line array of characters
    with open(FILEPATHREAD, "r") as fr:
        data = [float(number) for number in fr.read().split(" ")]

    # Creates output file and writes appropriate response to file and notifies user
    with open(FILEPATHWRITE, "w") as fw:
        fw.write(str(expected_value_calculator(data)))

    return print("\nThe Expected Offspring dataset has been processed and the appropriate output has been saved to {}.\n".format(FILEPATHWRITE[2:]))

if __name__ == "__main__":
    main()