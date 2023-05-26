#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Bio import SeqIO

#function to read in input sequence from fasta file and output

#def kmer(input_fa, kmer_length, output_txt, directionality, est_size, filter_kmer):

seq_file = "example_genome.fa"

#implement hashtable using dictionary
hashtable = {}

for sequ in SeqIO.parse(open(seq_file),'fasta'):
    sequence = str(sequ.seq)


print(sequence)
#count(sequence, hashtable, 6, True, 100, 3)


#function to generate hashtable with kmer counts

#def count(sequence, hashtable, kmer_length, ignore_directionality, est_size, filter_kmer):
kmer = 6
for i in range(len(sequence)-kmer+1):
    end = kmer + i
    kmer_key = sequence[i:end]
    hashtable[kmer_key] = hashtable.get(kmer_key, 0) + 1
    #if ignore_directionality:
        #kmer_key = ignore_directionality(sequence,kmer)
        
print(hashtable)

#function to generate reverse complement if directionality is ignored
def ignore_directionality(sequence, kmer):
    nucleotides = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    reverse_complement = ''.join(nucleotides[key] for key in reversed(sequence))
    return min(kmer, reverse_complement)

#output the kmer counts in a txt file
output_txt = "output.txt"
with open(output_txt, "w") as out_file:
    for kmer, count in hashtable.items():
            out_file.write(f"{kmer}\t{count}\n")


# In[2]:


from Bio import SeqIO

#function to read in input sequence from fasta file and output

#def kmer(input_fa, kmer_length, output_txt, directionality, est_size, filter_kmer):

seq_file = "example_genome.fa"

#implement hashtable using dictionary
hashtable = {}

for sequ in SeqIO.parse(open(seq_file),'fasta'):
    sequence = str(sequ.seq)

sequence = "GATTA"
print(sequence)
#count(sequence, hashtable, 6, True, 100, 3)


#function to generate hashtable with kmer counts

#def count(sequence, hashtable, kmer_length, ignore_directionality, est_size, filter_kmer):
kmer = 3
for i in range(len(sequence)-kmer+1):
    end = kmer + i
    kmer_key = sequence[i:end]
    hashtable[kmer_key] = hashtable.get(kmer_key, 0) + 1
    #if ignore_directionality:
        #kmer_key = ignore_directionality(sequence,kmer)
        
print(hashtable)

#function to generate reverse complement if directionality is ignored
def ignore_directionality(sequence, kmer):
    nucleotides = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    reverse_complement = ''.join(nucleotides[key] for key in reversed(sequence))
    return min(kmer, reverse_complement)

#output the kmer counts in a txt file
output_txt = "short_output.txt"
with open(output_txt, "w") as out_file:
    for kmer, count in hashtable.items():
            out_file.write(f"{kmer}\t{count}\n")


# In[11]:


# sequence parameter takes the user's sequence from which we should count kmers 
# kmer parameter takes user's desired kmer size
# output file follows format: kmer/tcount/n
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
            
    output_txt = "short_output.txt"
    with open(output_txt, "w") as out_file:
        for kmer, count in hashtable2.items():
            out_file.write(f"{kmer}\t{int(count)}\n")
    print(hashtable2)


# In[12]:


sequence = 'TATAATAT'
kmer = 4
ignore_directionality(sequence,kmer)


# In[29]:


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
    


# In[30]:


filter_low_freq('short_output.txt', 2)


# Example Run With A Short Sequence (5 Bases), expected hashtable will have 3 kmers if kmer length is 3
