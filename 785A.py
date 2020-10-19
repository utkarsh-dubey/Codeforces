n=int(input())
d={"Tetrahedron":4,"Cube":6,"Octahedron":8,"Dodecahedron":12,"Icosahedron":20}
sum=0
for i in range(n):
    
    s=str(input())
    sum+=d[s]
    
print(sum)