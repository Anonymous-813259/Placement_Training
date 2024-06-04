"""
in:-
    14
op:-
    17
    printing next prime number
    factors will be available till only half of that number.
"""

num=int(input())
if num==2:
    print(num)
else:
    if num%2==0:
        num+=1
    while(True):
        prime=True
        for i in range(2,(num//2)+1):
            if num%i==0:
                prime=False
                break
        if prime:
            print(num)
            break
        num+=2