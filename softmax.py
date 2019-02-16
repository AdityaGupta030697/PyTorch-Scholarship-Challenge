import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    tot = [np.e**i for i in L]
    s = np.sum(tot)
    ans = [i/s for i in tot]
    return ans
