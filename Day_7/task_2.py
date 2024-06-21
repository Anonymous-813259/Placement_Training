"""
ip:-
    string:- school
    n=3
    operation 1:- L 2 rotate left by 2 to string
    operation 2:- R 3 rotate right by 3 to string
    operation 3:- L 1 rotate left by 1 to string
    take first letters of each output
    and check whether it is an anagram of the subsequence string
op:-
    yes or no
"""
s=input()
n=int(input())
res=""
l=[]
length=len(s)
for i in range(n):
    op=input()
    #l.append(int(op[2:]))
    if op[0]=='L':
        res+=s[int(op[2:])]
    else:
        res+=s[(int(op[2:]))*-1]
print(res)
res="".join(sorted(res))
print(res)
sub_string=[]
res_len=len(res)
for i in range(length-res_len-1):
    sub_string.append("".join(sorted(s[i:i+res_len])))
print(sub_string)
flag=False
for i in sub_string:
    if i==res:
        print("Yes")
        flag=True
        break
if not flag:
    print("No")