"""
ip:-
    list with some numbers, those are the quantities of gold available in that house. A theif is planning to steel. If he steels in one house he won't steel exact next house. Find how much max gold can he steel.
    [13,9,4,10,5,7]
op:-
    30
"""
l=list(map(int,input().split()))
def rec_fun(l,s):
    if not l:
        return s
    return max(rec_fun(l[2:],s+l[0]),rec_fun(l[1:],s))
print(rec_fun(l,0))