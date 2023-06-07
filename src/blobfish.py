#!/usr/bin/env python
# coding: utf-8

# In[14]:


import argparse
from Blobfish_Functions import generateTable
import os
import sys
#from version import __version__
def main():
    parser=argparse.ArgumentParser(
        prog = "Blobfish",
        description = "Command line script to perform counting of Kmers <3"
    )
    
    #input
    parser.add_argument("-l","--length", help="length of kmer :)", type=int, required=True)
    parser.add_argument("-f", "--filename", help = "input your fasta file path :)", \
                        metavar="FILE", type=str, required = True)
    
    #other options

    #ignore directionality
    parser.add_argument("-canonical","--ignore_directionality", \
                        help="this option ignores the directionality of the sequence", \
                        action="store_true", default=False, required=False)

    #filter kmers
    parser.add_argument("-k","--filter_kmer", help="filter out kmers with a frequency lower than your input :D", \
                        type=int,metavar = "REG", default=0, required = False)
    
    #output
    parser.add_argument("-o", "--out", help="give your output file path here, include the filetype .txt!" \
                        "Default: stdout", metavar="FILE", type=str, required= True)
    
    #parse args
    args = parser.parse_args()
    
    generateTable(args.filename, args.length, args.out, args.ignore_directionality, args.filter_kmer)
    
if __name__ == "__main__":
        main()
