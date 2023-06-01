# CSE185_Group44
Implementing Jellyfish command to generate a table for kmer counts.

The tool will count the number of kmers in A DNA sequence. The user will be able to specify the desired length of the kmer as an  input to  output and count the number of kmers that meet that desired kmer length, for the kmer counting function itself. There is an option to ignore strand directionality while counting number of kmers. Additionally, the tool will be more precise by filtering out low-frequency kmers. The tool takes a fasta file as an input and outputs a text file containing the kmer counts and their respective names.


How to Run:
1) Instiall Biopython by using the command pip install biopython
2) Make a copy of the JellyFishCommand.ipynb file and the example_genome.fa file and run the Jupyter Notebook in a folder in Jupyter Notebook. You can also clone this repository using git clone and run our Jupyter notebook file and see that there is an outputted file with the kmer counts in the same folder.
