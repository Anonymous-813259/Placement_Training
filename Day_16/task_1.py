"""
ip:-
    number of queries
    number followed by word
op:-
    if number is 1 then insert the word
    if number is 2 then search for the word, found-> True, not found-> False
    if number is 3 then search for the word with the given prefix-> True or False

    7
    1 school
    1 world
    1 word
    1 scholar
    2 word
    2 wood
    3 sch
"""
n=int(input())
l=[]
unique_l=[]
for i in range(n):
    a,b=input().split()
    if a=="1":
        if b not in l:
            l.append(b)
    elif a=="2":
        if b in l:
            print(True)
        else:
            print(False)
    elif a=="3":
        n=len(b)
        """prefix_l=[]
        n=len(b)
        for i in l:
            prefix_l.append(i[:n])
        if b in prefix_l:
            print(True)
        else:
            print(False)"""
        count=0
        for i in l:
            if b==i[:n]:
                count+=1
        print(count)
    elif a=="4":
        l.remove(b)
