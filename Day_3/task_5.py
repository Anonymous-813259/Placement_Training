"""
ip:-
    take list from the user
    5 3 2 7 8 4
    m t w t f s
op:-
    price of pen changes from monday to saturday
    buy on one day sell on one day by the week do it for max profit
"""
l=list(map(int,input().split()))
max_porfit=0
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if l[j]-l[i]>max_porfit:
            max_porfit=l[j]-l[i]
print(max_porfit)

res=0
buy=l[0]
for i in range(1,len(l)):
    if l[i]-buy<0:
        buy=l[i]
    if res<l[i]-buy:
        res=l[i]-buy
print(res)