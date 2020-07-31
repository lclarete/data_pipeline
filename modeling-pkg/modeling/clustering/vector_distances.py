#!/usr/bin/env python
# coding: utf-8

# # Vector distances
# * https://machinelearningmastery.com/distance-measures-for-machine-learning/

# * __Hamming distance__ calculates the distance between two binary vectors, also referred to as binary strings or bitstrings for short.

# In[101]:


def hamming_distance(s1, s2) -> int:
    """return the Hamming distance between equal-length sequences"""
    if len(s1) != len(s2):
        raise ValueError('Undifined for sequences of unequal length')
    return sum(e1 != e2 for e1, e2 in zip(s1, s2))/len(s1)

from scipy.spatial.distance import hamming


# In[102]:


row1 = [0, 0, 0, 0, 0, 1]
row2 = [0, 0, 0, 0, 1, 0]

print(hamming_distance(row1, row2))
print(hamming(row1, row2))


# * __Euclidean distance__ calculates the distance between two real-valued vectors.

# In[108]:


from math import sqrt

def euclidean_distance(s1, s2):
    return sqrt(sum((e1 - e2)**2 for e1, e2 in zip(s1, s2)))

from scipy.spatial.distance import euclidean


# In[111]:


row1_int = [10, 20, 15, 10, 5]
row2_int = [12, 24, 18, 8, 7]

print(euclidean_distance(row1_int, row2_int))
print(euclidean(row1_int, row2_int))


# * __The Manhattan distance__, also called the Taxicab distance or the City Block distance, calculates the distance between two real-valued vectors.

# In[117]:


def manhattan_distance(s1, s2):
    return sum(abs(e1-e2) for e1, e2 in zip(s1, s2))

from scipy.spatial.distance import cityblock


# In[119]:


print(manhattan_distance(row1_int, row2_int))
print(cityblock(row1_int, row2_int))


# * Other types of distances: https://aiaspirant.com/distance-similarity-measures-in-machine-learning/
# 
# * https://medium.com/analytics-vidhya/types-of-distances-in-machine-learning-5b1233380775

# * __Kullback-Leibler (KL) divergence__
# Used in t-SNE; called Information Gain in decision trees

# In[ ]:




