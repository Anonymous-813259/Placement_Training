"""
ip:-
    given an array that contains coins 1,2,4,5 coins. all coins are infinite.
    How to make 15 rupees with minimum number of coins
    [1,2,4,5]
    15
    [1,3,4,5]
    17
op:-
    3
    4
"""

def rec_fun(l,cost,coin):
    if not l or cost<0:
        return 9999
    elif cost==0:
        if coin==0:
            return 9999
        return coin
    return min(rec_fun(l[1:],cost,coin),rec_fun(l,cost-l[0],coin+1))


l=[3,4]
cost=5
tab=[[0 for i in range(cost+1)] for j in range(len(l))]
for i in range(len(l)):
    for j in range(1,cost+1):
        if i==0 and j%l[i]==0:
            tab[i][j]=j//l[i]
        else:
            if j<l[i]:
                tab[i][j]=tab[i-1][j]
            elif j%l[i]==0:
                tab[i][j]=j//l[i]
            else:
                if tab[i][j-l[i]]!=0 and tab[i-1][j]!=0:
                    value=min(tab[i-1][j],1+tab[i][j-l[i]])
                elif tab[i][j-l[i]]!=0:
                    value=1+tab[i][j-l[i]]
                else:
                    value=tab[i-1][j]
                tab[i][j]=value

for i in tab:
    print(i)
if tab[-1][-1]==0:
    print(-1)
else:
    print(tab[-1][-1])

sir_tab=[-1 for i in range(cost+1)]
print()
print("Sir Tabulation Sheet:-")
print(sir_tab)
sir_tab[0]=0
for i in l:
    for j in range(i,cost+1):
        if j%i==0:
            sir_tab[j]=j//i
        if sir_tab[j-i]!=-1:
            sir_tab[j]=1+sir_tab[j-i]
print(sir_tab)
print(sir_tab[-1])