difficulty=[66,1,28,73,53,35,45,60,100,44,59,94,27,88,7,18,83,18,72,63]
profit=[66,20,84,81,56,40,37,82,53,45,43,96,67,27,12,54,98,19,47,77]
worker=[61,33,68,38,63,45,1,10,53,23,66,70,14,51,94,18,28,78,100,16]


tab_1_d=[0 for i in range(len(difficulty)+1)]
for i in range(len(worker)):
    for j in range(1,len(profit)+1):
        if difficulty[j-1]<=worker[i]:
            tab_1_d[j]=max(tab_1_d[j-1],tab_1_d[-1]+profit[j-1])
        else:
            tab_1_d[j]=tab_1_d[j-1]
print(tab_1_d[-1])

res=0
job_profit=sorted(zip(difficulty,profit))
worker.sort()
mx=0
j=0
print(job_profit)
print(worker)
for i in range(len(worker)):
    while j<len(job_profit) and job_profit[j][0]<=worker[i]:
        mx=max(mx,job_profit[j][1])
        j+=1
    if j<len(job_profit):
        print(mx,worker[i],job_profit[j])
    res+=mx
print(res)


"""d=dict()
for i in range(len(difficulty)):
    if profit[i] not in d:
        d[profit[i]]=difficulty[i]
    elif d[profit[i]]>difficulty[i]:
        d[profit[i]]=difficulty[i]
res=0
profit.sort(reverse=True)
for i in range(len(worker)):
    for j in range(len(profit)):
        #print(difficulty[j],worker[i])
        if d[profit[j]]<=worker[i]:
            res+=profit[j]
            break
print(res)"""



"""
d=dict()
for i in range(len(difficulty)):
    if difficulty[i] not in d:
        d[difficulty[i]]=profit[i]
    elif d[difficulty[i]]>profit[i]:
        d[difficulty[i]]=profit[i]
"""

"""
tab=[[0 for i in range(len(profit)+1)] for j in range(len(worker)+1)]
print("Initial Tabulation Sheet:- ")
for i in tab:
    print(i)
print()
for i in range(1,len(worker)+1):
    for j in range(1,len(difficulty)+1):
        #print(i-1,j-1)
        value=tab[i-1][-1]
        if difficulty[j-1]<=worker[i-1]:
            #value=tab[i-1][-1]+d[difficulty[j-1]]
            value+=profit[j-1]
        tab[i][j]=max(value,tab[i][j-1])
for i in tab:
    print(i)
print(tab[-1][-1])
"""