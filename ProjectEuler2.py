'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed n(input), find the sum of the even-valued terms.

t is the number of test cases.
'''
#!/bin/python3
import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    total=0
    prev,cur=0,1
    while cur<n:
        if cur%2==0:
            total+=cur
        prev,cur=cur,prev+cur
    print(total)