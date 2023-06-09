# CSE185_Group44

Implementing the Jellyfish command to generate a table with kmer counts.

Our implementation of a kmer counting command is blobfish, which is a command line tool that will output a table containing kmer-counts from a given sequence. Our tool takes in a fasta file, output file name, and the length of the kmers the user wants to count to output a .txt file containing the kmer keys and their respective counts. Our tool also has the option to ignore strand directionality using the option --canonical and the option to filter out kmers with frequencies lower than a certain value the user inputs through -k <frequency>.

__Command__: python blobfish.py -f &lt;filename&gt; -l &lt;kmer length&gt; -o &lt;output name&gt; [-canonical] [-k (filter kmers by output)] [-a (filter automatically)]

    options: -f = filename, with path defined (required)
             -l = kmer length (required)
             
             -canonical = if option is stated jellyfish will ignore directionality
             -k = filter kmer's with counts less than inputted value
             -a = filter kmers by an automatically generated value


__How to Run:__
1) Install Biopython by using the command 
    
        pip install biopython
2) Install our directory
   
        git clone https://github.com/##user##/CSE185_Group44.git
3) Change into the directory CSE185_Group44/src
   
        cd CSE185_Group44/src
4) Run the blobfish command! Here is an example:
    
        python blobfish.py -f ~/CSE185_Group44/example_genome.fa -l 6 -canonical -k 10 -o output.txt
    
__How to Benchmark__
    
    Please read the README file in the tests folder to find out how to benchmark our tool
    
 __About our Repo:__
    
    1) src folder : contains all of the functions that give blobfish its functionality

        - blobfish.py : the main() function for blobfish which takes command line arguments and runs our python function in Blobfish_Functions.py

        - Blobfish_Functions.py : the python script containing functions that calculate kmer count table with the given options

    2) tests folder : contains files and README regarding benchmarking

        - accuracy.py : file that computes accuracy score for kmer count table and histogram visualizations of benchmarking files
        - ebola_genome.fa : this is a fasta file containing the ebola virus partial genome Zaire ebolavirus isolate IRF0164

    3) setup.py : file for setting up blobfish package, would implement installable package in future directions
