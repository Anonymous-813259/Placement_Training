"""
ip:-
    now take consecutive 3 elements and sort them and then next three elements
    4 9 8 2 14 3 15 6
    i.e., 1st->4 9 8 => 4 8 9 2 14 3 15 6
    next with the updated one 2nd-> 8 9 2 => 4 2 8 9 14 3 15 6
    and so on
op:-
    4 2 8 3 5 6 9 14
"""
l=list(map(int,input().split()))
for i in range(len(l)-2):
    if l[i]<l[i+1] and l[i]<l[i+2]:
        if l[i+1]<l[i+2]:
            l[i],l[i+1],l[i+2]=l[i],l[i+1],l[i+2]
        else:
            l[i],l[i+1],l[i+2]=l[i],l[i+2],l[i+1]
    elif l[i+1]<l[i] and l[i+1]<l[i+2]:
        if l[i]<l[i+2]:
            l[i],l[i+1],l[i+2]=l[i+1],l[i],l[i+2]
        else:
            l[i],l[i+1],l[i+2]=l[i+1],l[i+2],l[i]
    else:
        if l[i]<l[i+1]:
            l[i],l[i+1],l[i+2]=l[i+2],l[i],l[i+1]
        else:
            l[i],l[i+1],l[i+2]=l[i+2],l[i+1],l[i]
print(l)