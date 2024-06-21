"""
reverse the number using reccursion and check for palindrome
"""

n=int(input())
def rec_fun(rev_num,num):
    if num==0:
        return rev_num
    return rec_fun((rev_num*10)+(num%10),num//10)
reverse_num=rec_fun(0,n)
print(reverse_num)
if reverse_num==n:
    print("Palindrome")
else:
    print("Not Palindrome")