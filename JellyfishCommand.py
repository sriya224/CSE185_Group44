#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from Bio import SeqIO

#function to generate hashtable with kmer counts
def count_kmers(sequence, hashtable, kmer_length, ignore_directionality, filter_kmer):
    kmer = 6
    for i in range(len(sequence)-kmer+1):
        end = kmer + i
        kmer_key = sequence[i:end]
        hashtable[kmer_key] = hashtable.get(kmer_key, 0) + 1
        #if ignore_directionality:
            #kmer_key = ignore_directionality(sequence,kmer)
        
    #print(hashtable)

# output file should be from previous commands in our program and contains calculated kmers and their frequencies
# threshold parameter is an integer value given by the user. Any kmer frequency lower than the threshold will be dropped
def filter_low_freq(outputfile, threshold):
    kmer_counts = {}
    
    with open(outputfile) as outputfile:
        outputlist = outputfile.read().splitlines()
    for x in outputlist: 
        mylist = x.split('\t',2)
        
        #print(mylist[0])
        print(threshold)
        print(mylist[1])
        if(int(mylist[1]) < int(threshold)):
            kmer_counts[mylist[0]] = int(mylist[1])
            
    with open(outputfile, "w") as out_file:
        for kmer, count in kmer_counts.items():
            outputfile.write(f"{kmer}\t{count}\n")
    print(kmer_counts)
    
#function to read in input sequence from fasta file and output

def kmer(input_fa, kmer_length, output, directionality, filter_kmer):

    seq_file = input_fa

    #implement hashtable using dictionary
    hashtable = {}

    for sequ in SeqIO.parse(open(seq_file),'fasta'):
        sequence = str(sequ.seq)

    #print(sequence)

    count_kmers(sequence, hashtable, kmer_length, True, True)
    
    #output the kmer counts in a txt file
    output_txt = output
    with open(output_txt, "w") as out_file:
        for kmer, count in hashtable.items():
                out_file.write(f"{kmer}\t{count}\n")




#function to generate reverse complement if directionality is ignored(still working on making this work)
def ignore_directionality(sequence, kmer):
    nucleotides = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    #reverse_complement = ''.join(nucleotides[key] for key in reversed(sequence))
    hashtable2 = {}
    
    for i in range(len(sequence)-kmer+1):
        end = kmer + i
        kmer_key = sequence[i:end]
        kmer_complement = ''.join(nucleotides[key] for key in reversed(kmer_key))
        print(kmer_complement)
        hashtable2[kmer_key] = hashtable2.get(kmer_key, 0) + 1
        hashtable2[kmer_complement] = hashtable2.get(kmer_complement, 0) + 1



seq_file = "example_genome.fa"
output_txt = "output.txt"
kmer(seq_file, 6, output_txt, True, True)

