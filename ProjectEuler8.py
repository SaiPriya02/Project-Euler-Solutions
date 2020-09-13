'''
Find the greatest product of k consecutive digits in the n digit number.
t is the number of test cases.
'''

#!/bin/python312
import sys

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    #num is the actual number
    maxprod=0
    for i in range(0,n-k):
        prod=1
        splits=num[i:i+k] #this is the sliced number

        #make it an int list (separate digits) and multiply
        for a in list(splits):
            a=int(a)
            prod*=a
        if maxprod<prod:
            maxprod=prod
    print(maxprod)