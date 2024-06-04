"""
ip:
    input with string of M and F only M-male and F-female
    "MMFFFMMFMFMMFMFMMF"
op:
    if M==F, print 0
    if M>F, print M
    if M<F, print F
"""
s=input()
c=0
for i in s:
    if i=='M':
        c+=1
    else:
        c-=1
if c==0:
    print(0)
elif c>0:
    print('M')
else:
    print('F')

#https://leetcode.com/problems/sorting-the-sentence/


"""i=0
j=-1
m=0
f=0
while id(s[i+1])!=id(s[j]) and id(s[i])!=id(s[j]):
    if s[i]=='M':
        m+=1
    else:
        f+=1
    if s[j]=='M':
        m+=1
    else:
        f+=1
    i+=1
    j-=1
    print(s[i],m,f,s[j],m,f)
if i+1==j:
    if s[i+1]=='M':
        m+=1
    else:
        f+=1
    if s[j]=='M':
        m+=1
    else:
        f+=1
else:
    if s[i]=='M':
        m+=1
    else:
        f+=1
    if s[j]=='M':
        m+=1
    else:
        f+=1
print(m,f)
if m==f:
    print(0)
elif m>f:
    print('M')
else:
    print('F')"""