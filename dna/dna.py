import csv
import sys


def main():

# TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

# TODO: Read database file into a variable
    sequences = []

    dnafile = {}
    with open(sys.argv[1]) as dictfile:
        for index, row in enumerate(dictfile):
            if index == 0:
                sequences = [sequence for sequence in row.strip().split(",")][1:]
            else:
                name = row.strip().split(",")
                dnafile[name[0]] = name[1:]

# TODO: Read DNA sequence file into a variable
    with open(sys.argv[2], "r") as txtfile:
        sqcfile = txtfile.read().replace('\n', '')

# TODO: Find longest match of each STR in DNA sequence
    result = [longest_match(sqcfile, subsequence) for subsequence in sequences]

# TODO: Check database for matching profiles
    for s in dnafile:
        count = 0
        for j in range(len(dnafile[s])):
            if result[j] == int(dnafile[s][j]):
                count += 1
        if count == len(sequences):
            return print(s)

    return print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    for i in range(sequence_length):

        # Initialize consecutive run count
        count = 0

        while True:

            # Adjust substring 
            start = i + count * subsequence_length
            end = start + subsequence_length

            if sequence[start:end] == subsequence:
                count += 1

            else:
                break


        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest
    return longest_run


main()
