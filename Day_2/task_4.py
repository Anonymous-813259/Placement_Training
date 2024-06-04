"""
print yes if list length is even
else no if list length is odd
"""
l=list(map(int,input().split()))
i=0
j=-1
while id(l[i+1])!=id(l[j]) and id(l[i])!=id(l[j]):
    #print(i,j)
    i+=1
    j-=1
if id(l[i])==id(l[j]):
    print("No")
else:
    print("Yes")


