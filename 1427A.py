from math import *
from collections import deque
from copy import deepcopy
import sys
def inp(): return sys.stdin.readline().rstrip("\r\n") #for fast input
def multi(): return map(int,input().split())
def lis(): return list(map(int, inp().split()))
def out(var): sys.stdout.write(str(var))  #for fast output, always take string
def printlist(a) :
    for p in range(0,len(a)):
        out(str(a[p]) + ' ')

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

t=int(input())
for _ in range(t):

    n=int(input())
    a=lis()
    b=[]
    sum=0
    flag=False
    present={}
    sum2=0
    for i in a:
        sum2+=i
    if(sum2==0):
        print("NO")
        continue
    # for i in a:
    #     if(i<0):
    #         b.append()
    a.sort()

    if(sum2>0):
        a=a[::-1]

    print("YES")
    printlist(a)
    print()
