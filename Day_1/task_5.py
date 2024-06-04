"""
ip:
    f46feLK9y56u#@&56hIjbn6KJhA
op:
    lv,uv,lc,uc,d,s
"""
s=input()
lv=0
uv=0
lc=0
uc=0
d=0
sp=0
for i in s:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        lv+=1
    elif i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
        uv+=1
    elif i>='a' and i<='z':
        lc+=1
    elif i>='A' and i<='Z':
        uc+=1
    elif i>='0' and i<='9':
        d+=1
    else:
        sp+=1

print("Lower Vowels:-",lv)
print("Upper Vowels:-",uv)
print("Lower Consonents:-",lc)
print("Upper Consonents:-",uc)
print("Digits:-",d)
print("Special Characters:-",sp)

#Only for special characters
sp_char=0
for i in s:
    if not ((i>='a' and i<='z') or (i>='A' and i<='Z') or (i>='0' and i<='9')):
        sp_char+=1
print("Special Characters:-",sp_char)


"""
organised way
for i in s:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        lv+=1
    elif i>='a' and i<='z': # if (i.islower()) --> for lowercase
        lc+=1
    elif i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
        uv+=1
    elif i>='A' and i<='Z': # elif (i.isupper()) --> for uppercase
        uc+=1
    elif i>='0' and i<='9': # elif (i.isdigit())
        d+=1
    else: # elif(not i.isalnum()):
        sp+=1

#more Organised way
for i in s:
    if(i.isupper()):
        if i in 'AEIOU':
            uv+=1
        else:
            uc+=1
    elif(i.islower()):
        if i in 'aeiou':
            lv+=1
        else:
        lc+=1
    elif(i.isdigit()):
        d+=1
    elif(not i.isalnum()):
        s+=1
"""