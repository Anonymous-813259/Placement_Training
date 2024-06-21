"""
ip:-
    take input from user i.e., that many queries.
    1st they will give the a to z alphabets in random order
    next number of queries of strings arrange them in sorted order with respect to the given order
    2
    polikujmnhytgbvfredcxswqaz
    abcd
    qwryupcsfoghjkldezxvbintma
    ativedoc
op:-
    bdca
    codevita
"""
n=int(input())
for i in range(n):
    order=input()
    string=input()
    d=dict()
    ord_len=len(order)
    str_len=len(string)
    for i in range(str_len):
        if i not in d:
            d[string[i]]=1
        else:
            d[string[i]]+=1
    res=""
    i=0
    while i!=ord_len:
        if order[i] in d and d[order[i]]!=0:
            res+=(order[i])*d[order[i]]
            d[order[i]]=0
        i+=1
    print()
    print("ans:-",res)
    print()