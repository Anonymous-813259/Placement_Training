"""
ip:-
    4
op:-
    ____a____
    ___aba___
    __abcba__
    _abcdcba_
"""
n=int(input())
for i in range(n):
    char='a'
    print("_"*(n-i),end="")
    for j in range(i+1):
        print(char,end="")
        char=chr(ord(char)+1)
    char=chr(ord(char)-2)
    for j in range(i):
        print(char,end="")
        char=chr(ord(char)-1)
    print("_"*(n-i))
