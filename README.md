# CSE185_Group44

Implementing the Jellyfish command to generate a table with kmer counts.

Our implementation of jellyfish is a command line tool that will output a table containing kmer-counts from a given sequence. Our tool takes in a fasta file, output file name, and the length of the kmers the user wants to count to output a .txt file containing the kmer keys and their respective counts. Our tool also has the option to ignore strand directionality using the option --cannonical and the option to filter out kmers with frequencies lower than a certain value the user inputs through -k <frequency>.

__Command__: python jellyfish.py -f &lt;filename&gt; -l &lt;kmer length&gt; -o &lt;output name&gt; [-cannonical] [-k <filter kmers>]

    options: -f = filename, with path defined (required)
             -l = kmer length (required)
             
             -cannonical = if option is stated jellyfish will ignore directionality
             -k = filter kmer's with counts less than inputted value


__How to Run:__
1) Instiall Biopython by using the command 
    
        pip install biopython
2) Install our directory
   
        git clone https://github.com/##user##/CSE185_Group44.git
3) Change into the directory CSE185_Group44
   
        cd CSE185_Group44
4) Run the jellyfish command! Here is an example:
    
        python Jellyfish.py -f ~/CSE185_Group44/example_genome.fa -l 6 -cannonical -k 10 -o output.txt
