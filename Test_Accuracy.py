#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
  
kmers = []
counts = []
  
f = open('outputBlob.txt','r')
for row in f:
    row = row.split('\t')
    kmers.append(row[0])
    counts.append(int(row[1]))
  
plt.bar(kmers, counts, color = 'g', label = 'File Data')
  
plt.xlabel('Kmers', fontsize = 12)
plt.ylabel('Counts', fontsize = 12)
  
plt.title('Kmer Counts', fontsize = 20)
plt.legend()
plt.show()

