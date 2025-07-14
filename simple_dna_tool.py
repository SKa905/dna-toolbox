#Complementary DNA sequence code (DNA Replication)
#NOTE - In the future want to add a feature that adds all instances of nucleotides that aren't A/C/U/G into a list with the respective positions
# of each error. Then I can add as part of my error message the positions of ALL instances of errors not just the first one that pops up.
# This logic will likely apply to the complement_RNA code as well.
dna_seq = input("Paste the DNA sequence you'd like to analyze here: ")
def complement_DNA(dna):
    """
    Inputs a DNA string consisting of A, C, T, G characters. Returns a list consisting of a complement DNA sequence, or Error messages showing positions at which input string doesn't consist of A, C, T, or G characters.
    """
    dna = dna.upper()
    complement_list = []
    error_list = []
    error_flag = False
    for i in range(len(dna)):
        if dna[i] == "A":
            complement_list.append("T")
        elif dna[i] == "T":
            complement_list.append("A") 
        elif dna[i] == "C":
            complement_list.append("G") 
        elif dna[i] == "G":
            complement_list.append("C")
        else:
            error_flag = True
            error_list.append(i+1)
    if error_flag:
        return (f"Error. Your DNA sequence has a nucleotide that doesn't exist at positions: {error_list}.\nMake sure it consists of either A, C, G, or T nucleotides.")
    else:
        return complement_list
    

#Complementary RNA sequence code (Transcription)
#NOTE - See complement_DNA comment
def complement_RNA(dna):
    """
    Inputs a DNA string consisting of A, C, T, G characters. Returns a list consisting of a complement RNA sequence, or Error messages showing positions at which input string doesn't consist of A, C, T, or G characters.
    """
    dna = dna.upper()
    complement_list = []
    error_list = []
    error_flag = False
    for i in range(len(dna)):
        if dna[i] == "A":
            complement_list.append("U")
        elif dna[i] == "T":
            complement_list.append("A") 
        elif dna[i] == "C":
            complement_list.append("G") 
        elif dna[i] == "G":
            complement_list.append("C")
        else:
            error_flag = True
            error_list.append(i+1)
    if error_flag:
        return (f"Error. Your DNA sequence has a nucleotide that doesn't exist at positions: {error_list}.\nMake sure it consists of either A, C, G, or T nucleotides.")
    else:
        return complement_list

#RNA Protein sequence code (Translation)
def translate(rna):
    """
    Inputs an RNA string consisting of A, U, G, C characters. Returns a list of proteins that would result from translating the RNA sequence into a primary-structure.
    """
    rna = ''.join(rna)
    translate_list = []
    for i in range(0, len(rna), 3):
        translate_list.append(rna[i:i+3])
    return translate_list

print(translate(complement_RNA(dna_seq)))