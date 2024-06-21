"""
ip:-
    list of numbers and k
op:-
    all k combinations
"""
l=list(map(int,input().split()))
res=[]
def fun_rec(l,s,i,k):
    if len(s)==k:
        res.append(s)
        return
    if i==len(l):
        return
    fun_rec(l,s+[l[i],],i+1,k)
    fun_rec(l,s,i+1,k)
    
k=3
fun_rec(l,[],0,k)
print(res)