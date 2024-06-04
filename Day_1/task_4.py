"""
in:
    3 5 4 3 6 7 1 2 4 3 3 7 6 8 8
out:
    3-4
    5-1
    4-2
    6-2
    7-2
    1-1
    2-1
    8-2
"""
l=list(map(int,input().split()))
d=dict()
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for key,vals in d.items():
    print(key,vals)