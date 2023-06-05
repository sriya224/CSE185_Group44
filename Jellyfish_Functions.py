#!/usr/bin/env python
# coding: utf-8

# In[17]:


from Bio import SeqIO

#function to read in input sequence from fasta file and output a file containing kmer table 
def generateTable(input_fa, kmer_length, output, directionality, filter_kmer):

    seq_file = input_fa

    #implement hashtable using dictionary
    hashtable = {}

    for sequ in SeqIO.parse(open(seq_file),'fasta'):
        sequence = str(sequ.seq)

    #print(sequence)
    
    if(directionality == True):
        ignore_directionality(sequence, kmer_length, hashtable)
    else:
        count_kmers(sequence, hashtable, kmer_length, filter_kmer)
    #FILTER
    if(filter_kmer > 0):
        hashtable = filter_low_freq(hashtable, filter_kmer)
    #output the kmer counts in a txt file
    output_txt = output
    #if user chooses to filter low frequencies call helper method, else output hashtable into txt file
    with open(output_txt, "w") as out_file:
        for kmer, count in hashtable.items():
                out_file.write(f"{kmer}\t{count}\n")

                

#function to generate hashtable with kmer counts without ignoring directionality
def count_kmers(sequence, hashtable, kmer_length, filter_kmer):
    #for every kmer of length kmer_length, push into hashtable and increment key if not unique
    for i in range(len(sequence)-kmer_length +1):
        end = kmer_length + i
        kmer_key = sequence[i:end]
        hashtable[kmer_key] = hashtable.get(kmer_key, 0) + 1
        
    #print(hashtable)

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



seq_file = "example_genome.fa"
output_txt = 'output_now.txt'
generateTable(seq_file, 6, output_txt, True, 18)


# In[ ]:




