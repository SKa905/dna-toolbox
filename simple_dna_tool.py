#Complementary DNA sequence code (DNA Replication)
#NOTE - In the future want to add a feature that adds all instances of nucleotides that aren't A/C/U/G into a list with the respective positions
# of each error. Then I can add as part of my error message the positions of ALL instances of errors not just the first one that pops up.
# This logic will likely apply to the complement_RNA code as well.
def complement_DNA(dna):
    dna = dna.upper()
    complement = ''
    for i in range(len(dna)):
        if dna[i] == "A":
            complement += "T"
        elif dna[i] == "T":
            complement += "A" 
        elif dna[i] == "C":
            complement += "G" 
        elif dna[i] == "G":
            complement += "C"
        else:
            return f"Error. Your DNA sequence has a nucleotide that doesn't exist at position {i+1}. Make sure it consists of either A, C, G, or T nucleotides."
    return complement

#Complementary RNA sequence code (Transcription)
#NOTE - See complement_DNA comment
def complement_RNA(dna):
    dna = dna.upper()
    complement = ''
    for char in dna:
        if char == "A":
            complement += "U"
        elif char == "U":
            complement += "A" 
        elif char == "C":
            complement += "G" 
        else:
            complement += "C"
    return complement

#RNA Protein sequence code (Translation)