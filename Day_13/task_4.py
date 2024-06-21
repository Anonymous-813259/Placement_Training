"""
ip:-
    given an array that contains coins 1,2,4,5 coins. all coins are infinite.
    How to make 15 rupees with minimum number of coins
    [1,2,4,5]
    15
op:-
    3

ip:-
    7262 sec
op:-
    2h:1m:2s
ip:-
    500 sec
op:-
    0h:
"""
"""seconds=int(input("Enter Seconds:- "))
h=0
m=0
if seconds>=3600:
    h=seconds//3600
    seconds=seconds%3600
if seconds>=60:
    m=seconds//60
    seconds=seconds%60
print(f"{h}Hr:{m}Mn:{seconds}Sec")"""


def rec_fun(l,cost,coin):
    if not l or cost<0:
        return 9999
    elif cost==0:
        if coin==0:
            return 9999
        return coin
    return min(rec_fun(l[1:],cost,coin),rec_fun(l,cost-l[0],coin+1))

#print("Enter different Coins:- ",end='')
l=[4,3,5]
cost=17
#l=[4,3,7]
#cost=16
l.sort(reverse=True)
#cost=int(input("Enter Final Cost:- "))
#flag=False
print(rec_fun(l,cost,0))
"""for i in range(len(l)):
    c=cost
    coin=0
    for j in range(i,len(l)):
        if l[j]<=c:
            coin+=c//l[j]
            c=c%l[j]
            print(c,coin,l[j])
    if c==0:
        flag=True
        print(coin)
        break
if not flag:
    print(-1)"""
