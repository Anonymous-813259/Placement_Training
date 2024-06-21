"""
ip:-
    array in increasing order and non prime numbers
    4 8 14 22 36 68
op:-
    largest prime number between l[i] and l[i-1]
    i.e., 4-8->7,8-14->13,14-22->19,22-36->31,31-68->67
    sum(7 13 19 31 67)=137
"""
def check_prime(num):
    flag=True
    for i in range(num//2,1,-1):
        if num%i==0:
            flag=False
            break
    return flag
l=list(map(int,input().split()))
i=1
s=0
while i<len(l):
    flag=0
    for j in range(l[i],l[i-1],-1):
        if check_prime(j):
            flag=j
            break
    if flag!=0:
        s+=flag
    i+=1
print(s)