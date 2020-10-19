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

a=str(inp())
b=str(inp())
hr=0
mini=0
flag=False
# print(int(a[3:5])-int(b[3:5]))
if(int(a[3:5])>=int(b[3:5])):
    mini=int(a[3:5])-int(b[3:5])
else:
    flag=True
    mini = 60-abs(int(a[3:5]) - int(b[3:5]))

if(int(a[0:2])>=int(b[0:2]) and (not flag or  not int(a[0:2])==int(b[0:2]))):
    if(flag):
        hr=int(a[0:2])-int(b[0:2])-1
    else:
        hr = int(a[0:2]) - int(b[0:2])

else:
    if(flag ):
        hr = 23-abs(int(a[0:2]) - int(b[0:2]))
    else:
        hr = 24 - abs(int(a[0:2]) - int(b[0:2]))


if(int(hr)<10):
    print("0"+str(hr),end="")
else:
    print(str(hr),end="")
print(":",end="")
if(mini<10):
    print("0"+str(mini),end="")
else:
    print(str(mini))
# print(str(hr)+":"+str(mini))