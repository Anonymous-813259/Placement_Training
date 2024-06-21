"""
ip:-
    a list contains tuples that is timings start time and end time
    and second list is the money you can earn when you work in that time interval.
    nums=[(1,3),(2,5),(4,6),(6,7),(5,8),(7,9)]
    s=[5,6,5,4,11,2]
    i.e., (1,3)means 1 to 3 o clock that gives 5rs
    (2,5) means 2 to 5 o clock that gives 6 rs
    (4,6) means 4 to 6 o clock that gives 5rs
    and goes on
op:-
    how much max profit can he do.
    17
"""
nums=[(1,3),(2,5),(4,6),(3,7),(5,8),(7,9)]
s=[5,6,5,20,11,2]
def max_profit_rec(nums,s,profit):
    if len(nums)==0:
        return profit+0
    elif len(nums)==1:
        #print(nums,profit+s[0])
        return profit+s[0]
    l1=[]
    s1=[]
    for i in range(1,len(nums)):
        if nums[i][0]>=nums[0][1]:
            l1.append(nums[i])
            s1.append(s[i])
    return max(max_profit_rec(nums[1:],s[1:],profit),max_profit_rec(l1,s1,profit+s[0]))
    """pro1=max_profit_rec(nums[1:],s[1:],profit)
    #print(nums,s,pro1)
    if l1:
        pro2=max_profit_rec(l1,s1,profit+s[0])
    else:
        pro2=profit+s[0]
    #print(nums,l1,s,pro2)
    return max(pro1,pro2)"""
def max_profit(nums,s):
    profit=s.copy()
    i=1
    j=0
    while i<len(nums):
        if nums[j][1]<=nums[i][0] and profit[i]<profit[j]+s[i]:
            profit[i]=profit[j]+s[i]
        j+=1
        if i==j:
            i+=1
            j=0
    return max(profit)

print(max_profit_rec(nums,s,0))
print(max_profit(nums,s))