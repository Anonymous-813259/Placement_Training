"""
ip:-
    [4,8,2,4,4,8,4]
op:-
    print number from above list where that number occurs should occur atleast equal or more than half of the list len
"""
l=list(map(int,input().split()))
seat=-1
vote_dif=0
for i in l:
    if seat==-1 or vote_dif==0:
        seat=i
        vote_dif+=1
    elif seat!=i:
        vote_dif-=1
print(seat)



"""d=dict()
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
n=len(l)
flag=False
for i in d.keys():
    if d[i]>n//2:
        print(i)
        flag=True
        break
if not flag:
    print("False")"""