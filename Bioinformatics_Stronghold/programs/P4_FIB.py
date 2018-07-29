"""
NAME:               Rabbits and Recurrence Relations (Bioinformatics Stronghold)
CONTRIBUTOR:        Aakash Sudhakar

PROBLEM:            A sequence is an ordered collection of objects (usually numbers), which are allowed to repeat. 
                    Sequences can be finite or infinite. Two examples are the finite sequence (π,√‾(−2),0,π) and 
                    the infinite sequence of odd numbers (1,3,5,7,9,…). We use the notation an to represent 
                    the n-th term of a sequence.

                    A recurrence relation is a way of defining the terms of a sequence with respect to the values 
                    of previous terms. In the case of Fibonacci's rabbits from the introduction, any given month 
                    will contain the rabbits that were alive the previous month, plus any new offspring. 
                    A key observation is that the number of offspring in any month is equal to the number of rabbits 
                    that were alive two months prior. As a result, if Fn represents the number of rabbit pairs alive after 
                    the n-th month, then we obtain the Fibonacci sequence having terms Fn that are defined by the 
                    recurrence relation Fn=Fn−1+Fn−2 (with F1=F2=1 to initiate the sequence). Although the sequence 
                    bears Fibonacci's name, it was known to Indian mathematicians over two millennia ago.

                    When finding the n-th term of a sequence defined by a recurrence relation, we can simply use 
                    the recurrence relation to generate terms for progressively larger values of n. This problem introduces 
                    us to the computational technique of dynamic programming, which successively builds up solutions by 
                    using the answers to smaller cases.

DATASET:            Positive integers n≤40 and k≤5.
OUTPUT:             The total number of rabbit pairs that will be present after n months, if we begin with 1 pair 
                    and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit 
                    pairs (instead of only 1 pair).

SAMPLE DATASET:     5 3
SAMPLE OUTPUT:      19

STATUS:             Submitted.
"""


from math import sqrt


def k_recurrence_relation(n, k):
    """ Calculates fibonacci sequence and returns appropriate result to main() """
    if n < 40: 
        if n == 0 or n == 1:
            return n
        else: 
            return k_recurrence_relation(n - 1, k) + k * k_recurrence_relation(n - 2, k)    # Recursive functional call for Fibonacci calculation
    else:
        return round((1 + sqrt(5))**n - (1 - sqrt(5))**n) / (2**n*sqrt(5))      # Approximates fibonacci sequence result for runtime

def main():
    """ Returns Fibonacci sum based on number of months (n) and number of rabbit litter pairs (k) """
    
    # NOTE: Requires being in parent repo ('pwd' must return up to directory '/Rosalind_Bioinformatics/Bioinformatics_Stronghold')
    FILEPATHREAD = "./datasets/P4_FIB-dataset.txt"
    FILEPATHWRITE = "./outputs/P4_FIB-output.txt"

    with open(FILEPATHREAD, "r") as fr:
        rr_args = fr.read().split(" ")

    with open(FILEPATHWRITE, "w") as fw:
        fw.write(str(k_recurrence_relation(int(rr_args[0]), int(rr_args[1]))))

    return print("\nThe recurrence relational dataset has been processed and the appropriate output has been saved to {}.\n".format(FILEPATHWRITE))

if __name__ == "__main__":
    main()