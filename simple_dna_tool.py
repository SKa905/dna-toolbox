#Complementary DNA sequence code (DNA Replication)
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
        return ''.join(complement_list)

#RNA Protein sequence code (Translation)
def codon_list(rna):
    """
    Inputs an RNA string consisting of A, U, G, C characters. Returns a list of codons that would result from translating the RNA sequence into a primary-structure.
    """
    codon_list = []
    start = 0
    for i in range(0, len(rna), 3):
        codon_list.append(rna[i:i+3])
    for e in range(len(codon_list)):
        if codon_list[e] == "AUG":
            start += e
            break
    return codon_list[start:]   

def start_codon(rna):
    """
    Inputs an RNA string of A, U, G, C characters. Returns an integer, telling at what position (1 being the very first nucleotide) the start codon begins at.
    """
    rna = ''.join(rna)
    codon_list = []
    start_number = 1
    for i in range(0, len(rna), 3):
        codon_list.append(rna[i:i+3])
    for i in range(len(codon_list)):
        if codon_list[i] == "AUG":
            start_number = (3*i)
            break
    return start_number+1

print(f"\n--------------\nOriginal DNA sequence: {dna_seq}\n--------------")
print(f"Transcribed RNA sequence: {complement_RNA(dna_seq)}")
print(f"Start codon begins at position {start_codon(complement_RNA(dna_seq))}\n--------------")
print(f"Codon list to be translated: {codon_list(complement_RNA(dna_seq))}\n--------------")