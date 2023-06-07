#!/usr/bin/env python
# coding: utf-8

# In[17]:

###This file contains all of the functions that are used to run our blobfish method###

# import needed packages
from Bio import SeqIO

## This function reads a sequence from the inputted fasta file and outputs a file containing the desired kmer count table
    ## PARAMETERS: 
    # input_fa: the user given fasta file
    # kmer_length: int with the number of bases that are in each kmer 
    # output: the user given output text file 
    # directionality: boolean value to either consider directionality or not 
    # filter_kmer: int value with the threshold value for filtering, if filtering is specified by the user 
def generateTable(input_fa, kmer_length, output, directionality, filter_kmer, filter_rec):

    # Seq_file has input fasta file's data
    seq_file = input_fa

    #implement hashtable using dictionary
    hashtable = {}

    # Extract the sequence from the fasta file
    # Utilizes the SeqIO package 
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
    # If both filter options are chosen, override filter by count and only filter by recommended
    # Else if filter by recommended option is chosen run filter_auto() else run filter_count()
    if(filter_kmer > 0 & filter_rec):
        print('filter by count will be overidden, filter by recommended ')
        
    if(filter_rec):
        hashtable = filter_auto(hashtable)
    elif(filter_kmer > 0):
        hashtable = filter_count(hashtable, filter_kmer)
    
    ## OUTPUT
    # write final kmer counts into user specified output file
    output_txt = output
    with open(output_txt, "w") as out_file:
        for kmer, count in sorted(hashtable.items()):
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
	# Parameters: 
	# sequence: DNA sequence from which to count kmers
	# kmer_length: int with the number of bases that are in each kmer 
	# hashtable: data structure to store the counted kmers. key = kmer string, value = kmer count
def ignore_directionality(sequence, kmer_length, hashtable):
    # reference dictionary that maps each nucleotide to its complement 
    nucleotides = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    # iterate over sequence to count kmers 
    for i in range(len(sequence)-kmer_length+1):
        end = kmer_length + i
	# for each kmer, store its string value and its reverse complement’s string value 
        kmer_key = sequence[i:end]
        kmer_complement = ''.join(nucleotides[key] for key in reversed(kmer_key))
	# stores the lexicographically smaller kmer out of kmer and kmer_complement in the hash table 
	# increments / adds either kmer_key or kmer_complement, never both
        if kmer_key < kmer_complement:
            hashtable[kmer_key] = hashtable.get(kmer_key, 0) + 1
        else: 
            hashtable[kmer_complement] = hashtable.get(kmer_complement, 0) + 1

## Function to filter out low frequency kmers according to the threshold value 
	# Parameters: 
	# hashtable: dictionary to store the counted kmers. key = kmer string, value = kmer count
	# threshold: any kmers that have a count that is less than or equal to the threshold will be filtered out
def filter_count(hashtable, threshold):
    mylist = []
    # dictionary that will store all kmers that are above threshold 
    outputhash = {}
    # iterate through every kmer in the hash table
    for key, value in hashtable.items(): 
	# stores the current kmer key and value 
        mylist = [key,value]
	# if the current kmer’s count is greater than the threshold, keep it and store it in outputhash 
        if(int(mylist[1]) > int(threshold)):
            outputhash[mylist[0]] = mylist[1]
    # assign outputhash which contains unfiltered kmers back to the original hashtable to return 
    hashtable = outputhash
    return hashtable

## Function to filter out low frequency kmers automatically
	# Parameters:
	# hashtable dictionary to store the counted kmers. key = kmer string, value = kmer count
def filter_auto(hashtable):
    # dictionary that will store counts as the key and number of kmers with that count as the value
    outputhash = {}
    # iterate through all the kmers in the inputted hashtabl
    # create a new dictionary where key = count and value = number of kmers
    # add to the new dictionary / increment for each kmer 
    for key, value in hashtable.items(): 
        if value in outputhash:
            outputhash[value] += 1
        else:
            outputhash[value] = 1
            
    # call find_valley helper function to find the first place where the number of kmers start increasing 
    valleycount = find_valley(outputhash)
    
    # for user to know what find_valley found to be the optimal filtering threshold
    print("Your recommended filtering count is" + str(valleycount))
    
    # if no valley was found, notify the user that all the kmer counts are the same and break out of the function 
    if(valleycount == None):
        print("All kmer counts are the same!, no filtering is needed")
        return
    
    # List to store keys to be deleted
    keys_to_delete = []  
    
    # check if count of each kmer is less than valley value, and if so add it to a list of kmers to be deleted 
    for key, value in hashtable.items():
        if value <= valleycount:  
            keys_to_delete.append(key)   

    # delete all necessary kmers from the inputted hashtable and return
    for key in keys_to_delete:
        del hashtable[key]

    return hashtable
        
## This function is a helper method for find_auto that finds the first place where the number of kmers starts increasing
def find_valley(hashtable):
    valley = list(hashtable.values())[0]
    for key in hashtable:
        if(hashtable[key] - valley > 0):
            return key
        valley = hashtable[key]

# In[ ]:




