"""
ip:-
    take list from user, that contains duplicated values.
    ip1:- 2 2 3 1 1 1 4 2 3 5

    ip2:- 1 2 3 4 1 2 3 1 2

    ip3:- 2 3 1 3 4 3 2
op:-
    return a 2d list such that each row should not contain duplicate values
    op1:- [2 3 1 4 5
           2 1 3
           1 2
           1]

    op2:- [1 2 3 4
           1 2 3
           1 2]
        
    op3:- [2 3 1 4
           3 2
           3]
"""
l=list(map(int,input().split()))
res=[]
while l:
    new_list=[]
    d=dict()
    row=[]
    for i in l:
        if i not in d:
            d[i]=1
            row.append(i)
        else:
            new_list.append(i)
    l=list(new_list)
    res.append(list(row))

#print(res)
for i in res:
    print(i)


"""#Sir Code
a=[]
m=[]
c=0
while(c!=len(a)):
    r=[]
    for i in range(len(a)):
        if (not a[i].isalpha()):
            if (a[i] not in r):
                c=c+1
                r.append(a[i])
                a[i]='a'
    m.append(r)
print(m)"""