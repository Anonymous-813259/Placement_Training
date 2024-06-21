"""
ip:-
    7
    0 5 3 6 7 2 1
op:-
    4
    find missing number in the given range
"""
n=int(input())
l=list(map(int,input().split()))
actual_s=((n)*(n+1))//2
s=0
for i in l:
    s+=i
print(actual_s-s)