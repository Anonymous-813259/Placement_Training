"""
ip:-
    5
op:-
    * * * * *
    * 1 2 3 *
    * 4 5 6 *
    * 7 8 9 *
    * * * * *
"""
n=int(input())
last_num=(n-2)**2
num=1
for i in range(n):
    if i==0 or i==n-1:
        print("* "*n)
        continue
    for j in range(n):
        if j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(num,end=" ")
            num+=1
    print()
