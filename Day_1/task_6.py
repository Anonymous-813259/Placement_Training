"""
in:
    placements
op:
    plAcEmEnts
in:
    School
op:
    schOOl
"""
s=input()
res=""
for i in s.lower():
    if i in 'aeiou':
        res+=i.upper()
    else:
        res+=i.lower()
print(res)