capital=[0,1,2]
profits=[1,2,3]
k=3
w=0

d=dict()
for i in range(len(capital)):
    if capital[i] not in d:
        d[capital[i]]=[profits[i],]
    else:
        d[capital[i]].append(profits[i])
cap=w
while k!=0:
    profit=d[capital[cap]].pop()
    w+=profit
    cap=w
    k-=1
    while cap>=0 and (cap not in d or d[cap]==[]):
        cap-=1

print(w)