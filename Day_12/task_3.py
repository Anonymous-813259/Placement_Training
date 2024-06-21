"""
ip:-
    two lists mixture of even and odd numbers size will be same
    6 3 2 9 4 7
    8 7 5 3 6 9
op:-
    addition of even number of first list and odd number of second list and odd numbers of first list with even numbers of second list
    13, 11, 9, 15, 11, 9, 9, 7, 5, 11, 17, 15, 11, 9, 7, 13, 15, 13
    next
    add the even numbers of first element with odd numbers of second element and before going to next even number of the first element add the res and make one
    i.e., 6+7=13,6+5=11,6+3=9,6+9=15, next 13+11+9+15=48
    then go to next even element
    48 48 40
"""
#res=[]
def rec_fun(l1,l2,i,j,res,s):
    if j==len(l2):
        i+=1
        j=0
    if i==len(l1):
        return res
    if l1[i]%2==0 and l2[j]%2!=0:
        s+=l1[i]+l2[j]
    elif l1[i]%2!=0 and l2[j]%2==0:
        res.append(l1[i]+l2[j])
    return rec_fun(l1,l2,i,j+1,res,s)
def rec_fun1(l1,l2,i,j,res,s):
    if j==len(l2):
        i+=1
        j=0
        if s!=0:
            res.append(s)
        s=0
    if i==len(l1):
        return res
    if l1[i]%2==0 and l2[j]%2!=0:
        s+=l1[i]+l2[j]
    #elif l1[i]%2!=0 and l2[j]%2==0:
    #    res.append(l1[i]+l2[j])
    return rec_fun1(l1,l2,i,j+1,res,s)



l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
res=rec_fun1(l1,l2,0,0,[],0)
print(res)