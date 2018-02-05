"""exercise.py"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from Bio import SeqIO


def computeGeneStats(filename):
    geneInfo = pd.read_csv(filename, sep="\t", header = 0)
    genes = geneInfo[ geneInfo["feature"] == "gene"] 
    #print(genes.head())
    print("{} genes present".format(genes.shape[0]))
    #print(genes.head())
    avg = np.mean(genes["end"] - genes["start"])
    print("Avg gene length: {:.2f}".format(avg))
    #print(genes.columns)
    grpd = genes.groupby(["Chr"])
    countByChr = dict()
    for i,g in grpd:
        #print("Group: ", i)
        countByChr[i] = genes[genes["Chr"] == i ].shape[0]
    #print(countByChr)
    #agg = grpd.aggregate(pd.DataFrame.value_counts())
    h = pd.Series([countByChr[x] for x in countByChr.keys()], index = countByChr.keys()).sort_index()
    h.sort_index()
    h.plot(kind = 'bar')
    plt.ylabel("# Genes")
    plt.xlabel("Chr")
    plt.show()
    return geneInfo

def printSequence(geneInfo, geneID, sequenceFile):
        gn = "gene:" + geneID
        gene = geneInfo[geneInfo["ID"] == gn]
        
        if(len(gene) > 0):
            seqDict = SeqIO.to_dict(SeqIO.parse(sequenceFile, "fasta"))
            chr = gene.iloc[0]["Chr"]
            start = gene.iloc[0]["start"]
            end = gene.iloc[0]["end"]
            print("Gene {} is in {} and has length {}".format(geneID,chr, end-start))
            if(chr in seqDict):
                s = seqDict[chr].seq[start-1:end]
                print(">"+geneID)
                print(s)
            else:
                print(chr, "is not present in the sequence file.")
            
        else:
            print("GeneID {} is not present in the input file.".format(geneID))



fn = "gene_models.tsv"
seqFile = "sequences.fasta"

GenesDF = computeGeneStats(fn)
printSequence(GenesDF,"MD05G1027300",seqFile)
print("")
printSequence(GenesDF,"MD03G1000400",seqFile)
print("")
printSequence(GenesDF,"MD08G1000100",seqFile)
print("")
printSequence(GenesDF,"MD08G100019191",seqFile)
