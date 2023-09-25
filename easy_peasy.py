from pwn import *

flag = "51124f4d194969633e4b52026f4c07513a6f4d05516e1e50536c4954066a1c57"
text="03464b4f1a1c3a313d1951573d195102383d1907533d1905033d1904043d1904"


encrypted_flag = bytes.fromhex(flag)
encrypted_text = bytes.fromhex(text)
decode = b'a'*32

key = xor(encrypted_text, decode) 
print(xor(encrypted_flag, key).decode())
