#Complementary DNA sequence code (DNA Replication)
dna_seq = input("Paste the DNA sequence you'd like to analyze here: ")

def complement_DNA(dna):
    """
    Inputs a DNA string consisting of A, C, T, G characters. Returns a string consisting of a complement DNA sequence, or Error messages showing positions at which input string doesn't consist of A, C, T, or G characters.
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
        return ''.join(complement_list)
    
#Complementary RNA sequence code (Transcription)
def complement_RNA(dna):
    """
    Inputs a DNA string consisting of A, C, T, G characters. Returns a string consisting of a complement RNA sequence, or Error messages showing positions at which input string doesn't consist of A, C, T, or G characters.
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
def start_codon(rna):
    """
    Inputs an RNA string or list of A, U, G, C characters. Returns an integer, telling at what position (1 being the very first nucleotide) the start codon begins at.
    """
    rna = ''.join(rna)
    for i in range(len(rna)):
        if rna[i:i+3] == "AUG":
            return i+1
    return "Error! There is no start codon present in this DNA sequence."

def codon_list(rna):
    """
    Inputs an RNA string or list consisting of A, U, G, C characters. Returns a list of codons that would result from translating the RNA sequence into a primary-structure.
    """
    codon_list = []
    if type(start_codon(rna)) != int:
        return "N/A"
    else:
        for i in range(start_codon(rna)-1, len(rna), 3): # type: ignore
            codon_list.append(rna[i:i+3])
        if len(codon_list[-1]) < 3:
            del (codon_list[-1])
        return codon_list


#OUTPUT CODE
print(f"--------------\nAssuming DNA is being replicated by DNA Polymerase:\n")
print(f"Original DNA sequence: \n{dna_seq}\n")
print(f"Complement DNA strand: \n{complement_DNA(dna_seq)}\n--------------")

print(f"Assuming DNA will eventually become a protein sequence:\n")
print(f"Original DNA sequence: \n{dna_seq}\n")
print(f"Transcribed RNA sequence: \n{complement_RNA(dna_seq)}.\nStart codon begins at position: {start_codon(complement_RNA(dna_seq))}\n")
print(f"Codon list to be translated: \n{codon_list(complement_RNA(dna_seq))}\n--------------")