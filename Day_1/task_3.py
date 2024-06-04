'''"""
in:
    aaabbaaaaddd
op:
    a3b2a4d3
"""
s=input()
count=1
res=""
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        count+=1
    else:
        res+=s[i-1]+str(count)
        count=1
    """print(s[i],count)"""
res+=s[-1]+str(count)
print(res)
'''

j=0
while(j<2):
    i=2
    j+=1
print(i)


for i in range(3):
    pass
print(i)