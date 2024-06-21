"""
ip:-
    take two numbers input
op:-
    find co-primes or not
"""
a=int(input())
b=int(input())
mn=min(a,b)
flag=True
for i in range(2,(mn//2)+1):
    if a%i==0 and b%i==0:
        flag=False
if flag and a%mn==0 and b%mn==0:
    flag=False
print(flag)