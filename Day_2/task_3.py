"""
return sum of all even numbers from 1 to n using recursion
"""
n=int(input())
def even_sum(n,i,s):
    if i>n:
        return s
    if i%2==0:
        s+=i
    return even_sum(n,i+2,s)

flag=False
if n<0:
    n=n*-1
    flag=True
if flag==True:
    print((even_sum(n,2,0))*-1)
else:
    print(even_sum(n,2,0))