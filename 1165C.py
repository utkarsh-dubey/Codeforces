n=int(input())
s=""
i=0
j=1
a=input()
while j<n:
	if a[i]==a[j]:
		j+=1
	else:
		s+=a[i]+a[j]
		i=j+1
		j+=2
print(n-len(s))
print(s)