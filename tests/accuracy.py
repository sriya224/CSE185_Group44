# function to benchmark actual jellyfish command with our implementation
# IMPORTANT: Look at the useage example in the bottom of the file and modify it with your output filenames. 
# IMPORTANT: Make sure file1 = jellyfish outuput and fille2 = blobfish output
import matplotlib.pyplot as plt

# Function to compute accuracy of kmer count tables as well as generate histogram visualizations of kmer distributions
def accuracy(file1, file2):
  
    # Create a histogram plot to visualize kmer-count trends for jellyfish command (kmers on x axis will be hard to read with large data sets)
    kmers = []
    counts = []

    f = open(file1,'r')
    for row in f:
        if '>' in row: 
            counts.append(int(row[1:]))
        else: 
            kmers.append(row)

    plt.bar(kmers, counts, color = 'm', label = 'File Data')

    plt.xlabel('Kmers', fontsize = 12)
    plt.ylabel('Counts', fontsize = 12)

    plt.title('Kmer Counts for Jellyfish', fontsize = 20)
    plt.legend()
    plt.show()
    
    # Create a histogram plot to visualize kmer-count trends for blobfish command (kmers on x axis will be hard to read with large data sets)
    kmers = []
    counts = []

    f = open(file2,'r')
    for row in f:
        row = row.split('\t')
        kmers.append(row[0])
        counts.append(int(row[1]))

    plt.bar(kmers, counts, color = 'm', label = 'File Data')

    plt.xlabel('Kmers', fontsize = 12)
    plt.ylabel('Counts', fontsize = 12)

    plt.title('Kmer Counts Blobfish', fontsize = 20)
    plt.legend()
    plt.show()
    
    compare_kmer_counts(file1, file2)

# Function to compare each kmer and its count with both files
def compare_kmer_counts(file1, file2):
    kmer_counts1 = {}
    kmer_counts2 = {}
    
    # Read file1
    # Add kmers and matching count into kmer_counts1 dictionary
    with open(file1) as file1:
        count = None
        for line in file1:
            line = line.strip()
            if line.startswith('>'):
                count = int(line[1:])
            elif count is not None:
                kmer = line
                kmer_counts1[kmer] = count
                count = None
    
    # Read file2
    # Add kmers and matching count into kmer_counts2 dictionary
    with open(file2) as f2:
        for line in f2:
            line = line.strip()
            if line:
                kmer, count = line.split('\t')
                line = line
                kmer_counts2[kmer] = int(count)
    # Compute total number of kmers
    total_kmers = len(kmer_counts1)
    if total_kmers == 0:
        return 0
    
   # Compare kmer counts, increment matching_kmers value if blobfish kmer count is equal to jellyfish kmer count
    matching_kmers = 0
    total_kmers = len(kmer_counts1)
    for kmer, count in kmer_counts1.items():
        if kmer in kmer_counts2 and kmer_counts2[kmer] == count:
            matching_kmers += 1
    
   # Calculate percentage accuracy
    accuracy = matching_kmers / total_kmers * 100
    print(f"Accuracy: {accuracy:.2f}%")
    return accuracy

# Usage example
# Expect the code to take a while 
file1 = "real_jellyfishrequired.txt"
file2 = "blobfish_required.txt"
accuracy(file1, file2)
