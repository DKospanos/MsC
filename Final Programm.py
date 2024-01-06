def is_valid_sequence(dna_sequence):
    valid_nucleotides = set("ATCGatcg")
    # if char != ' '  is in order to ignore spaces that might mistakenly be in the sequence
    return all(char in valid_nucleotides for char in dna_sequence if char != ' ')


def find_coding_regions(dna_sequence):
    if not is_valid_sequence(dna_sequence):
        print("Invalid DNA sequence.")
        return []

    start_codon = "ATG"
    stop_codons = ["TAA", "TAG", "TGA"]

    coding_regions_found = []
    # .upper()  so it will read both in lower and upper cases
    start_index = dna_sequence.upper().find(start_codon)
    # if ATG not found it will show -1
    while start_index != -1:
        for stop_codon in stop_codons:
            # replace(' ', '') is to replace any unwanted spaces between nucleotides
            stop_index = dna_sequence.upper().replace(' ', '').find(stop_codon, start_index)
            # Check if the distance between start codon and stop codon is a multiple of 3
            if stop_index != -1 and (stop_index - start_index) % 3 == 0:
                coding_part = dna_sequence[start_index:stop_index + 3]
                coding_regions_found.append(coding_part)
                break

        start_index = dna_sequence.find(start_codon, start_index + 1)

    return coding_regions_found


given_sequence = input("Give a DNA sequence :")
coding_regions = find_coding_regions(given_sequence)

if coding_regions:
    print("Coding Regions:")
    for coding_region in coding_regions:
        print(coding_region)
else:
    # without this if in case of invalid sequence it will show both messages
    if is_valid_sequence(given_sequence):
        print("No coding region found in this sequence.")
