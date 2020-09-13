'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers which is less than n
t is the number of test cases.
'''
#!/bin/python3

import sys
plist=[]
for i in range(100,1000):
    for j in range(100,1000):
        num=i*j
        if str(num) == str(num)[::-1] and num not in plist: #n%11==0
            plist.append(num)
plist.sort()
length=len(plist)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    for i in range(length-1,-1,-1):
        if plist[i]<n:
            print(plist[i])
            break