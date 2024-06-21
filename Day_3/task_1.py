"""
ip:-
    input is string with only alphabets.
    and key also input
    string:- khoor #Encrypted String
    key:- 3 #Key to decrypted
op:-
    Decode the string
    res:- hello #Decrypted String
"""
encrypted_string=input()
key=int(input())
decrypted_string=""
for i in range(len(encrypted_string)):
    decrypted_string+=chr((((ord(encrypted_string[i])-97)-key)%26)+97)
print(decrypted_string)
