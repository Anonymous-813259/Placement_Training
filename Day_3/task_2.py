"""
ip:-
    "xyzabcdefklmnopqefgh"
op:-
    Longest substring in sequence
"""
s=input()
res_len=0
temp_res_len=1
for i in range(1,len(s)):
    if ord(s[i-1])+1==ord(s[i]):
        temp_res_len+=1
    elif res_len<temp_res_len:
        res_len=temp_res_len
        temp_res_len=1
if res_len<temp_res_len:
    res_len=temp_res_len
print(res_len)
