'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below n.

t is the number of test cases.
'''
#!/bin/python3
import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    #code here
    sum3=(n-1)//3
    sum5=(n-1)//5
    sum15=(n-1)//15

    print((3*(sum3*(sum3+1))//2)+(5*(sum5*(sum5+1))//2)-(15*(sum15*(sum15+1))//2))