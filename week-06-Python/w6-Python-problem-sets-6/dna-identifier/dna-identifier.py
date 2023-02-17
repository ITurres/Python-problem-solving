import csv
import sys

def main():
    # Check for command-line usage
    while True:
        if len(sys.argv) != 3:
            sys.exit("Usage: python dna.py CSV-file text.txt ")
        else:
            break

    # Read database file into a variable
    str_database = []
    with open(sys.argv[1]) as str_database_file:
        database_reader = csv.DictReader(str_database_file)
        for data in database_reader:
            str_database.append(data)

    # Read DNA sequence file into a variable
    # dna_sequence = list(open(sys.argv[2]))#!X
    with open(sys.argv[2], "r") as dna_sequence_file:
        dna_sequence = dna_sequence_file.read()

    # Find longest match of each STR in DNA sequence
    for data in str_database:
        STR_sequence = list(data.keys())[1:]  # stores just the STR strings e.g['AGATC', 'AATG', 'TATC'] not 'name'
        break

    STR_results = {}
    for STR in STR_sequence:
        STR_results[STR] = str(longest_match(dna_sequence, STR))

    # Check database for matching profiles
    for person_data in str_database:
        has_match = 0
        for STR in STR_results:
            # print(person_data[STR], " --- ", STR_results[STR])
            if person_data[STR] == STR_results[STR]:
                # print("HAS MATCH ==========> ", person_data[STR], " --- ", STR_results[STR])
                has_match += 1

        if has_match == len(STR_sequence):
            print(person_data["name"])
            return

    print("No match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""
    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):
        # Initialize count of consecutive runs
        count = 0
        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:
            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count) # always on column 8! otherwise wont throw right numbers
        # print(f"longest_run = {longest_run}")
    # After checking for runs at each character in sequence, return longest run found
    return longest_run


main()
