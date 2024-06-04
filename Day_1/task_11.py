"""
ip:-
    password
op:-
    minimum number of characters to add to fulfil password conditions
    length-8
    upper-1
    lower-1
    digit-1
    special-1
"""
password=input()
length=0
upper=1
lower=1
digit=1
special=1
"""for i in password:
    if i.isupper():
        upper=0
    elif i.islower():
        lower=0
    elif i.isdigit():
        digit=0
    elif not i.isalnum():
        special=0
    if upper==0 and lower==0 and digit==0 and special==0:
        break
    
        OR
"""
#uppercase
for i in password:
    if i.isupper():
        upper=0
        break
#lowercase
for i in password:
    if i.islower():
        lower=0
        break
#digits
for i in password:
    if i.isdigit():
        digit=0
        break
#special characters
for i in password:
    if not i.isalnum():
        special=0
        break
#Length of password
if len(password)>=8:
    length=-1
else:
    length=8-len(password)

if length==-1 and upper==0 and lower==0 and digit==0 and special==0:
    print(-1)
elif length>(upper+lower+digit+special):
    print(length)
else:
    print(upper+lower+digit+special)
