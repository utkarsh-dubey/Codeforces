from math import *
from collections import deque
from copy import deepcopy
import sys
def inp(): return sys.stdin.readline().rstrip("\r\n") #for fast input
def multi(): return map(int,input().split())
def strmulti(): return map(str, inp().split())
def lis(): return list(map(int, inp().split()))
def lcm(a,b): return (a*b)//gcd(a,b)
def ncr(n,r): return factorial(n) // (factorial(r) * factorial(max(n - r, 1)))
def stringlis(): return list(map(str, inp().split()))
def out(var): sys.stdout.write(str(var))  #for fast output, always take string
def printlist(a) :
    print(' '.join(str(a[i]) for i in range(len(a))))

def isPrime(n) :
    if (n <= 1) : return False
    if (n <= 3) : return True
    if (n % 2 == 0 or n % 3 == 0) : return False
    i = 5
    while(i * i <= n) :
        if (n % i == 0 or n % (i + 2) == 0) :
            return False
        i = i + 6
    return True

#copied functions end

#start coding

n,k=multi()

a=[]

for i in range(n):
    a.append(list(str(input())))

# print(a)
temp=[]
ans=0
for i in range(n-1):
    for j in range(k-1):
        temp=[a[i][j],a[i+1][j],a[i][j+1],a[i+1][j+1]]
        # print(temp)
        if(temp.count('f')==1 and temp.count('a')==1 and temp.count('c')==1 and temp.count('e')==1):
            ans+=1

print(ans)








