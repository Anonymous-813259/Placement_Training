"""
ip:-
    2 3 5 6
op:-
    11
"""
l=list(map(int,input().split()))
cost=int(input())
def rec_fun(l,cost):
    if cost==0:
        return True
    elif cost<0 or not l:
        return False
    return rec_fun(l[1:],cost) or rec_fun(l[1:],cost-l[0])

print(rec_fun(l,cost))

tab=[-1 for i in range(cost+1)]
prev_tab=[-1 for i in range(cost+1)]
prev_tab[0]=0
tab[0]=0
for i in range(len(l)):
    j=l[i]
    print(j)
    while j<cost+1:
        if l[i]==j:
            tab[j]=1
        else:
            if prev_tab[j-l[i]]!=-1:
                tab[j]=1+prev_tab[j-l[i]]
            else:
                tab[j]=prev_tab[j]
        j+=1
    prev_tab=tab.copy()
print(tab[-1])











"""tab=[-1 for i in range(cost+1)]
tab[0]=0
for i in range(len(l)):
    #print(tab)
    for j in range(l[i],cost+1):
        if j==l[i]:
            tab[j]=1
        elif tab[j-l[i]]!=-1:
            tab[j]=(1+tab[j-l[i]])
            print(l[i],j)
    #print(tab,l[i])
if tab[-1]==-1:
    print(False)
else:
    print(True)"""

"""
l.sort()
i=-1
j=0
temp=cost
c=0
"""
"""if cost not in l:
    while i!=j and temp!=c:
        #print(c,l[i],l[j])
        if c<temp and j<len(l):
            c+=l[j]
            if i==-1:
                i=0
            j+=1
        elif c>temp:
            c-=l[i]
            i+=1
        else:
            break
    #print(c,l[i],l[j])
    if c==temp:
        print("Yes")
    else:
        print("No")
else:
    print("Yes")"""