"""
given a number. add the digits untill you get a single digit. If it is a prime number then print the number direct
"""
d=dict()
d[2]=1
d[3]=1
d[5]=1
d[7]=1
res=-1
inp=int(input())
sum_value=inp
while len(str(sum_value))!=1:
    s=0
    for i in str(sum_value):
        s+=int(i)
    sum_value=s
while sum_value!=9 and sum_value not in d:
    sum_value+=1
    inp+=1
if sum_value==9:
    print(inp+2)
else:
    print(inp)





    
'''def check_prime(n):
    num=n
    #Adds till you get single number
    while len(str(num))!=1:
        s=0
        for i in str(num):
            s+=int(i)
        num=s
    #if sum not prime then add 1 to sum and n and check sum is prime or not
    #if sum prime directly return n
    #else if sum reached 9 add 2 to sum and n the return
    while num!=9 and num not in d:
        num+=1
        n+=1
    if num==9:
        return n+2
    else:
        return n
    """if num in d:
        return n
    else:
        return -1"""'''
'''res=-1
inp=int(input())
#print(check_prime(inp))
"""while True:
    res=check_prime(inp)
    if res!=-1:
        print(inp)
        break
    else:
        inp+=1"""
sum_value=inp
while len(str(sum_value))!=1:
    s=0
    for i in str(sum_value):
        s+=int(i)
    sum_value=s
while sum_value!=9 and sum_value not in d:
    sum_value+=1
    inp+=1
if sum_value==9:
    print(inp+2)
else:
    print(inp)'''