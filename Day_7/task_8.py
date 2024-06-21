"""
leetcode practice 6
"""
s="PAYPALISHIRING"
numRows=3
res=""
def rec_fun(s,next_character,j):
    print(s,next_character,j)
    if j>=len(s):
        return ""
    else:
        return s[j]+rec_fun(s,next_character,j+next_character)
for i in range(numRows):
    print(s,(numRows-(i+1))+(numRows-(i+1)),i)
    if i==numRows-1:
        print("3",s,(numRows-1)+(numRows-1),i)
        res+=rec_fun(s,(numRows-1)+(numRows-1),i)
    else:
        res+=rec_fun(s,(numRows-(i+1))+(numRows-(i+1)),i)
print(res)
#return res