"""
ip:-
    3
    3x3 matrix
    xyz
    pqr
    abc
    "yraxpazr"
op:-
    yes
rules:
    one elements should be taken from one row next time it should be from next row element can be repeated
"""

size=int(input())
matrix=[]
for i in range(size):
    row=list(input().split())
    matrix.append(row)
s=input()
row_num=0

"""Sir Idea
for i in s:
    if i not in matrix[row_num]:
        print("No")
        break
    row_num=(row_num+1)%size
else:
    print("Yes")
"""

row_record=dict()
flag="yes"

"""Sir Idea
print(matrix)
for i in s:
    if i not in matrix[row_num]:
        flag="No"
        break
    else:
        matrix[row_num].remove(i)
    row_num=(row_num+1)%size
print(matrix)"""

for i in s:
    if i not in matrix[row_num]:
        flag="No"
        break
    else:
        if row_num not in row_record:
            row_record[row_num]=i
        elif i in row_record[row_num]:
            flag="No"
            break
        elif i not in row_record[row_num]:
            row_record[row_num]+=i
    row_num=(row_num+1)%size
print(flag)

"""flag="Yes"
d=dict()
temp='abcdefghijklmnopqrstuvwxyz'
for i in temp:
    d[i]=0
size=int(input())
matrix=[]

for i in range(size):
    row=list(input().split())
    matrix.append(row)
    for j in row:
        d[j]=len(matrix)-1

s=input()
prev_ind=d[s[0]]
for i in range(1,len(s)):
    if (prev_ind+1)%size!=d[s[i]]:
        flag="No"
        break
    else:
        prev_ind=d[s[i]]
print(flag)"""

