from Bio import SeqIO
import numpy as np
from matplotlib import pyplot as plt




def loadData(filename):
        dataArray = []
        lID = ""
        lVal = -1
        sID= ""
        sVal = -1
        
        for seq_record in SeqIO.parse(filename, "fasta"):
            L = len(seq_record)
            dataArray.append(L)
            if( lVal == -1 or L >= lVal):
                if(lVal == L):
                    lID +="," + seq_record.id
                else:
                    lID = seq_record.id
                lVal = L
            if( sVal == -1 or L <= sVal):
                if(sVal == L):
                    sID +="," + seq_record.id
                else:
                    sID = seq_record.id
                sVal = L
                
        data  = np.array(dataArray)
        print("The file \"{}\" contains {} sequences\n".format(filename, data.size))
        print("Longest contig(s): {} (len: {:,})".format(lID,lVal))
        print("Shortest contig(s): {} (len: {:,})\n".format(sID,sVal))
        print("Mean size: {:.2f} base pairs".format(np.mean(data)))
        print("Median size: {:.2f} base pairs\n".format(np.median(data)))
        
        return data

def computeNX(data, X):
    if(X <0 or X> 1):
        print("Error:\nIt is impossible to compute N{}.\nOnly values between 0 and 1 are admitted for X".format(int(X*100)))
    else:
        data = np.sort(data)[::-1]
        cumS = np.cumsum(data)
        total = cumS[-1]
        val = 0
        ind = 0
        valCnt = data.size
        while cumS[ind] < total*X and ind < valCnt-1:
            ind += 1

        NX = data[ind + 1] # +1 because first bigger than N%!

        print("Total sequence size: {:,} base pairs".format(total))
        print("N{}: {:,} base pairs\n".format(int(X*100),NX))

        plt.bar(list(range(len(data))),data)
        plt.axhline(NX, color='r', ls='--', label="N{}".format(int(X*100)))
        plt.xlabel("Contig N")
        plt.ylabel("Contig size [bps]")
        plt.legend()

        plt.show()
          
              


              
lens = loadData("sequences.fasta")
for x in [-0.1, 0.2, 0.5, 0.8, 0.9, 1.1]:
    computeNX(lens,x)
