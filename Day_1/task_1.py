"""
inp: --> Sorted List will be given as input
    2 5 7 9
    1 3 6 7 10 13
out:
    1 2 3 5 6 7 7 9 10 13
"""
#time complexity for below code is O(m+n)
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=[]
m,n=len(l1),len(l2)
i=0
j=0
max_len=0
if m>n:
    max_len=m
else:
    max_len=n
while(i<m or j<n):
    if i<m and j<n:
        if l1[i]<l2[j]:
            l3.append(l1[i])
            i+=1
        elif l1[i]>l2[j]:
            l3.append(l2[j])
            j+=1
        else:
            l3.append(l1[i])
            l3.append(l2[j])
            i+=1
            j+=1
    elif i>=m and j<n:
        l3.append(l2[j])
        j+=1
    elif i<m and j>=n:
        l3.append(l1[i])
        i+=1
print(l3)