"""exercise.py"""

from Bio import SeqIO
import matplotlib.pyplot as plt


def computeKmers(seq, kmerLen, kmers):
    """given a DNA sequence seq and an integer kmers size 
    returns a dictionary with all kmers and their multiplicity in the string
    """
    
    if(kmerLen < len(seq)):
        for x in [seq[i:i + kmerLen ] for i in range(len(seq) - kmerLen + 1)  ]:
            
            if(x in kmers):
                kmers[x] += 1
            else:
                kmers[x] = 1
    
    return kmers

def parseFasta(fileName,kmerLen):
    """
    reads the fasta file : fileName
    constructs the dictionary with all the kmers
    having length kmerLen
    and returns the dictionary 
    """

    cnt = 0
    kmers = dict()
    for seq_record in SeqIO.parse(fileName, "fasta"):
        cnt += 1
        seq = str(seq_record.seq)
        computeKmers(seq,kmerLen, kmers)
        
    print("Read {} sequences.\nTotal number of {}mers: {}".format(cnt,kmerLen,len(kmers)))
    return kmers




def plotKmerSpectrum(kmers):
    """
     Given a dictionary kmers (i.e. keys are kmer sequences and 
     values are the number of occurrences of the kmer sequence) plots 
     the kmer spectrum of all the kmers present in the dictionary. 
     The kmer spectrum is a histogram of the multiplicities of all kmers. 
    """
    
    
    kmerSpect = dict()
    
    for k in kmers:
        mult = int(kmers[k])
        oldVal = kmerSpect.get(mult,0)
        kmerSpect[mult] = oldVal + 1
    
    #print(kmerSpect)
    xVals = []
    yVals = []
    for val in kmerSpect:
            xVals.append(val)
            yVals.append(kmerSpect[val])
    plt.plot(xVals,yVals)
    plt.xlabel("Multiplicity")
    plt.ylabel("Occurrences")
    plt.show()
    plt.close()

    
#seq = "AATAACTAGC"
#twoMers = dict()
#computeKmers(seq, 2, twoMers)
#print(twoMers)    
    
seq = "AATTAATTAACTAGCCTTAA"
twoMers = dict()
print("sequence:" , seq)
computeKmers(seq, 2, twoMers)
print(twoMers)
print("kmerSpect:")
plotKmerSpectrum(twoMers)
fourMers = dict()
computeKmers(seq, 4, fourMers)
print("4mers")
print(fourMers)
t2Mers = dict()
computeKmers(seq, 32, t2Mers)
print("32mers")
print(t2Mers)

#s = "ATATCACATCTG"
#s1 = "CTGACATATAT"
#print(s)
#print(s1)
#nt = dict()
#computeKmers(s, 4, nt)
#print(nt)
#computeKmers(s1, 4, nt)
#print(nt)


myFile = "shortSample.fasta"
kmers = parseFasta(myFile,4)
print(kmers)


myFile = "test_reads_75k.fasta"
kmers = parseFasta(myFile,17)
plotKmerSpectrum(kmers)
