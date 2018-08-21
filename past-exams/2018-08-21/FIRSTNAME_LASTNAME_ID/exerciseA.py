from Bio import SeqIO
import numpy as np
from matplotlib import pyplot as plt


def loadData(filename):
    raise Exception("TODO IMPLEMENT ME !")

def computeNX(data, X): 
    raise Exception("TODO IMPLEMENT ME !")
          
              

lens = loadData("sequences.fasta")
for x in [0.2, 0.5, 0.8, 0.9]:
    computeNX(lens,x)
