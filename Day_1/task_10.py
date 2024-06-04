"""
ip:-
    7854
op:-
    number of single prime digits = 2
"""
s=input()
count=0
for i in s:
    if i=='2' or i=='3' or i=='5' or i=='7':
        count+=1
print(count)