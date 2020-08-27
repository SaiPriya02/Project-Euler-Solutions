'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number n ?
'''
#!/bin/python3
#This is my optimal solution. 6/6 test cases passed (on Hackerrank)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    i = 2
    largest_prime = 2
    while i*i <= n:
        while n % i == 0:
            largest_prime = i
            n //= i    
        i += 1
    if n>largest_prime:
        largest_prime = n
    print(largest_prime)

'''
#This is my soution using brute force. 4/6 test cases passed
import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    flag,prime=0,0
    
    #first find factors
    factor=[1] #first factor
    for i in range(2,n//2+1):
        if n%i==0:
            factor.append(i)
    factor.append(n) #number itself
    #now check if they're prime
    for i in range(len(factor)):
        num=factor[len(factor)-i-1] #starts at last element
        flag=0
        for j in range(2,num//2): #to check if num is prime or not
            #print(j) 
            if num%j==0:
                flag=1 #not prime
                break
        if flag==0: #prime
            prime=num #largest prime since we're starting from the end of factor
            break
    print(prime) '''