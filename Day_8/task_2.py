"""
ip:-
    take input from the user input may contain lowercase, uppercase, digits and special characters
op:-
    check all alphabets present in the string or not
"""
d=dict()
alpha="qwertyuioplkjhgfdsazxcvbnm"
s=input()
for i in s:
    if i!=" ":
        d[i]=1
flag=True
for i in alpha:
    if i.isalpha() and 'a'<=i<='z' and i not in d:
        flag=False
        break
print(flag)