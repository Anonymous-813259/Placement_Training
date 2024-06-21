"""
ip:-
    take number from user
op:-
    print it as sum of 2 primes and consider 1 as prime
"""
n=int(input())
d=dict()
d[1]=1
d[2]=1
d[3]=1
d[5]=1
d[7]=1
def check_prime(num,i):
    if num in d or i==1:
        if i==1:
            d[num]=1
        return True
    if num%i==0:
        return False
    return check_prime(num,i-1)

def prime_pair(num,left,right):
    if left>right:
        return False
    if check_prime(left,left//2) and check_prime(right,right//2):
        return True
    return prime_pair(num,left+1,right-1)

print(prime_pair(n,1,n-1))