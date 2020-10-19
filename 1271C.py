from sys import stdin, stdout
n,h,k=map(int,input().split())
o=[h,k]
a=[]
for i in range(n):
	a.append(list(map(int,stdin.readline().split())))
maxi=0
l=0
r=0
u=0
d=0

final=[0,0]

for i in a:

	if(i[0]<=o[0]-1):
		

		l+=1
		
	if(i[0]>=o[0]+1):
		
		r+=1
		
	if(i[1]>=o[1]+1):
		u+=1

	if(i[1]<=o[1]-1):
		d+=1

maxi=max(r,l,u,d)

if(maxi==r):
	final[0]=o[0]+1
	final[1]=o[1]
if(maxi==l):
	final[0]=o[0]-1
	final[1]=o[1]
if(maxi==u):
	final[0]=o[0]
	final[1]=o[1]+1
if(maxi==d):
	final[0]=o[0]
	final[1]=o[1]-1



		




print(maxi)
print(final[0],final[1])







