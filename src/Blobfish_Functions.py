#!/usr/bin/env python
# coding: utf-8

# In[17]:

###This file contains all of the functions that are used to run our blobfish method###

# import needed packages
from Bio import SeqIO

## This function reads a sequence from the inputted fasta file and outputs a file containing the desired kmer count table
# Parameters: 
# input_fa: the user given fasta file
# kmer_length: int with the number of bases that are in each kmer 
# output: the user given output text file 
# directionality: boolean value to either consider directionality or not 
# filter_kmer: int value with the threshold value for filtering, if filtering is specified by the user 
def generateTable(input_fa, kmer_length, output, directionality, filter_kmer):

    # seq_file has input fasta file's data
    seq_file = input_fa

    #implement hashtable using dictionary
    hashtable = {}

    # extract the sequence from the fasta file
    # utilizes the SeqIO package 
    for sequ in SeqIO.parse(open(seq_file),'fasta'):
        sequence = str(sequ.seq)
    
    ## IGNORE DIRECTIONALITY
    # call ignore_directionality function to count kmers if the user has specified the ignore directionality option
    if(directionality == True):
        ignore_directionality(sequence, kmer_length, hashtable)
    # Otherwise, call count_kmers which counts without considering the reverse strand 
    else:
        count_kmers(sequence, hashtable, kmer_length)
        
    ## FILTER
    # if the user specified a threshold value to filter by in their command, then call filter_low_freq
    if(filter_kmer > 0):
        hashtable = filter_low_freq(hashtable, filter_kmer)
    
    ## OUTPUT
    # write final kmer counts into user specified output file
    output_txt = output
    with open(output_txt, "w") as out_file:
        for kmer, count in hashtable.items():
                out_file.write(f"{kmer}\t{count}\n")

                

## Function to generate hashtable with kmer counts (this does not ignore directionality / consider the reverse strand when counting)
# Parameters: 
# sequence: DNA sequence from which to count kmers
# hashtable: data structure to store the counted kmers. key = kmer string, value = kmer count 
# kmer_length: int with the number of bases that are in each kmer 
def count_kmers(sequence, hashtable, kmer_length):
    # iterate through sequence and for every kmer of length kmer_length, push it into the hashtable
    # only unique kmer values are stored, the value of the kmer is incremented if more than one exists
    for i in range(len(sequence)-kmer_length +1):
        end = kmer_length + i
        kmer_key = sequence[i:end]
        hashtable[kmer_key] = hashtable.get(kmer_key, 0) + 1
        

## Function to count kmers while ignoring directionality / considering the reverse strand when counting
# Parameter 
# sequence parameter takes the user's sequence from which we should count kmers 
# kmer parameter takes user's desired kmer size
def ignore_directionality(sequence, kmer_length, hashtable):
    nucleotides = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    
    for i in range(len(sequence)-kmer_length+1):
        end = kmer_length + i
        kmer_key = sequence[i:end]
        kmer_complement = ''.join(nucleotides[key] for key in reversed(kmer_key))

        if kmer_key < kmer_complement:
            hashtable[kmer_key] = hashtable.get(kmer_key, 0) + 1
        else: 
            hashtable[kmer_complement] = hashtable.get(kmer_complement, 0) + 1

#function to filter out low frequency kmers
# output file should be from previous commands in our program and contains calculated kmers and their frequencies
# threshold parameter is an integer value given by the user. Any kmer frequency lower than the threshold will be dropped
# output file should be from previous commands in our program and contains calculated kmers and their frequencies
# threshold parameter is an integer value given by the user. Any kmer frequency lower than the threshold will be dropped
# output file should be from previous commands in our program and contains calculated kmers and their frequencies
# threshold parameter is an integer value given by the user. Any kmer frequency lower than the threshold will be dropped
def filter_low_freq(hashtable, threshold):
    inside = False
    mylist = []
    outputhash = {}
    for key, value in hashtable.items(): 
        mylist = [key,value]

        #print(mylist)
        if(int(mylist[1]) > int(threshold)):
            inside = True
            outputhash[mylist[0]] = mylist[1]
        
    hashtable = outputhash
    return hashtable



# In[ ]:




