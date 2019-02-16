import numpy as np

# Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.
def cross_entropy(Y, P):
    ce = 0
    for i,j in zip(Y,P):
        if i==1:
            ce = ce -np.log(j)
        else:
            ce = ce - np.log(1-j)
            
    return ce        
