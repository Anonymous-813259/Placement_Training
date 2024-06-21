"""
ip:-
    tu5g2k1h8
    g5g8gd6h3
    take all unique numbers present in the above strings
op:-
    largest possible even number with the numbers in string
    865312
"""
#s1=input()
#s2=input()
s1="tu5g2k1h8"
s2="g5g8gd6h3"
d=dict()
for i in s1:
    if i.isnumeric() and i not in d:
        d[i]=1
for i in s2:
    if i.isnumeric() and i not in d:
        d[i]=1
str_num=list(d.keys())
str_num.sort(reverse=True)
if int(str_num[-1]!=0):
    i=len(str_num)-1
    while i>-1:
        if int(str_num[i])%2==0:
            break
        i-=1
    str_num=str_num[:i]+str_num[i+1:]+list(str_num[i])
print("".join(str_num))
