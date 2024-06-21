"""
ip:-
    3 5 9 6 8 10
"""
l=list(map(int,input().split()))
res1=0
res2=0
mx_height=0
for i in range(len(l)):
    if mx_height<l[i]:
        res1+=1
        mx_height=l[i]
mx_height=0
for i in range(len(l)-1,-1,-1):
    if mx_height<l[i]:
        res2+=1
        mx_height=l[i]
print(res1,res2)
