"""
using recursion print sum of even numbers with two lists
ip:
    a=[3,8,5,4,3]
    b=[5,0,9,3,2]
op:
    (a list even sum, b list odd sum)
"""
a=list(map(int,input().split()))
b=list(map(int,input().split()))

def even_odd_sum_combine(even_list,odd_list,even_sum,odd_sum):
    #if elements exist in even_list
    if len(even_list)!=0:
        if even_list[0]%2==0:
            even_sum+=even_list[0]
    #if elements exist in odd_list
    if len(odd_list)!=0:
        if odd_list[0]%2==1:
            odd_sum+=odd_list[0]
    #returning tuple if both lists are empty
    if len(even_list)==0 and len(odd_list)==0:
        return ((even_sum,odd_sum))
    #recalling the function
    return even_odd_sum_combine(even_list[1:],odd_list[1:],even_sum,odd_sum)

def even_odd_sum(l,s,type):
    if len(l)==0:
        return s
    if type=='e' and l[0]%2==0:
        s+=l[0]
    elif type=='o' and l[0]%2!=0:
        s+=l[0]
    return even_odd_sum(l[1:],s,type)
print((even_odd_sum(a,0,'e'),even_odd_sum(b,0,'o')))
print(even_odd_sum_combine(a,b,0,0))
