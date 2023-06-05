import matplotlib.pyplot as plt
  
kmers = []
counts = []
  
f = open('jellyfishoutput.txt','r')
for row in f:
    if '>' in line: 
        counts.append(int(row[1:]))
else: 
    kmers.append(row)
  
plt.bar(kmers, counts, color = 'g', label = 'File Data')
  
plt.xlabel('Kmers', fontsize = 12)
plt.ylabel('Counts', fontsize = 12)
  
plt.title('Kmer Counts for Jellyfish', fontsize = 20)
plt.legend()
plt.show()
