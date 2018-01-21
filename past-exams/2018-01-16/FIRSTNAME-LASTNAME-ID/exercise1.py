"""
Name:
Surname:
Matricola:
""""

from Bio import SeqIO
import matplotlib.pyplot as plt


def computeKmers(seq, kmerLen, kmers):
    """given a DNA sequence seq and an integer kmers size 
    returns a dictionary with all kmers and their multiplicity in the string
    """
    
    raise Exception("TODO IMPLEMENT ME !")


def parseFasta(fileName,kmerLen):
    """
    reads the fasta file : fileName
    constructs the dictionary with all the kmers
    having length kmerLen
    and returns the dictionary 
    """
    raise Exception("TODO IMPLEMENT ME !")


def plotKmerSpectrum(kmers):
    """
     Given a dictionary kmers (i.e. keys are kmer sequences and 
     values are the number of occurrences of the kmer sequence) plots 
     the kmer spectrum of all the kmers present in the dictionary. 
     The kmer spectrum is a histogram of the multiplicities of all kmers. 
    """
    raise Exception("TODO IMPLEMENT ME !")
    
    

