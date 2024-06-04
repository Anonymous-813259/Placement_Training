"""
in:
    300
    400
op:
    15

(limit2//7)-(limit1//7)
print count of divisible by 7 btw range
"""
a=int(input())
b=int(input())
count=0
for i in range(a,b+1):
    if i%7==0:
        count+=1
print(count)

ao=7*round(a/7)
an=7*round(b/7)
print(((an-ao)//7)+1)