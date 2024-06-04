"""
ip:-
    5 3.8 7 5.6 4 2 3
op:-
    Odd Sum:- 15
    Even Sum:- 6
    Float Sum:- 9.4

int(element)==element
if . in element
int%1==0
float%1!=0
"""
l=list(map(float,input().split()))
es=0
os=0
fs=0
for i in l:
    if int(i)==i:
        if i%2==0:
            es+=i
        else:
            os+=i
    else:
        fs+=i
print("Even Sum:-",int(es))
print("Odd Sum:-",int(os))
print("Float Sum:-",round(fs,4))