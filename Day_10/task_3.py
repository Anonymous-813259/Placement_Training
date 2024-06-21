"""
ip:-
    hello:5438,car:214,book:8799,apple:2187
    length of word in number then place that character if length of word not in number then take next small number near to length and keep that character if it is not their then place x
    hello length=5 5 in 5438 so o
    car length=3 3 not in 214 next small is 2 2 in 214 so a
    book length=4 4 not in 8799 next small is not their so x
op:-
    oaxp
"""
line_arr=list(input().split(','))
d=dict()
for i in line_arr:
    d[i.split(':')[0]]=i.split(':')[1]
res=""
for i in d:
    if str(len(i)) in d[i]:
        res+=i[-1]
    else:
        for j in range(len(i)-1,0,-1):
            if str(j) in d[i]:
                res+=i[j-1]
                break
        else:
            res+='x'
print(res)
