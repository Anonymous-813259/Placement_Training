m=2
k=3
#bloomDay=[1,10,3,10,2]
#bloomDay=[97,83]
bloomDay=[7,7,7,7,12,7,7]

l=[]
for i in range(len(bloomDay)-k+1):
    l.append(max(bloomDay[i:i+k]))
print(l)
min_day=[]
while l:
    mn=10000000000
    mn_ind=-1
    print(l)
    for i in range(len(l)):
        if mn>l[i]:
            mn=l[i]
            mn_ind=i
    min_day.append(mn)
    temp_k=k-1
    while temp_k:
        if mn_ind+1<len(l):
            l.pop(mn_ind+1)
        else:
            break
        temp_k-=1
    l.pop(mn_ind)
    temp_k=k-1
    while temp_k:
        if mn_ind-1>=0:
            l.pop(mn_ind-1)
        else:
            break
        temp_k-=1
    print(mn_ind)
    print(l)
    print(min_day)
print(max(min_day[:m]))


"""if m*k<=len(bloomDay):
    count=0
    while m>0:
        mn=10000000000
        for i in range(len(bloomDay)):
            if bloomDay[i]!=0:
                mn=min(mn,bloomDay[i])
        for i in range(len(bloomDay)):
            if bloomDay[i]!=0:
                bloomDay[i]-=mn
        print(mn)
        print(bloomDay)
        temp_k=k
        temp_m=m
        for i in range(len(bloomDay)):
            if bloomDay[i]==0:
                temp_k-=1
            else:
                temp_k=k
            if temp_k==0:
                temp_k=k
                temp_m-=1
            if temp_m==0:
                m=0
                break
        count+=mn
    print(count)
else:
    print(-1)"""