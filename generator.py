from math import log2, floor 
import torch

def count_bits(bin):
    cnt=0 
    b = bin 
    if bin == 0:
        return 0 
    
    for _ in range(floor(log2(bin)) + 1): 
        cnt += 1 if b % 2 else 0 
        b >>= 1

    return cnt 

def build_adj(n):
    a = torch.zeros(2**n, 2**n)
    for i in range(2**n):
        for j in range(i, 2**n):
            if count_bits(i ^ j) == 2:
                a[i][j] = a[j][i] = 1 
    
    return a 