"""
in:
    4 5 6 1 2 3 4 8 9 10 12
out:
    4
"""

l=list(map(int,input().split()))
max_seq=0
seq_1=1
for i in range(1,len(l)):
    if l[i-1]+1==l[i]:
        seq_1+=1
    else:
        if max_seq<seq_1:
            max_seq=seq_1
        seq_1=1
    """print(l[i-1],l[i])
    print(" ",seq_1,max_seq)"""
if max_seq<seq_1:
    max_seq=seq_1
print(max_seq)
        