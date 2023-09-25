import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
	return enc

def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]

flag = "a"
key = "a"
assert all([k in ALPHABET for k in key])
assert len(key) == 1

b16 = b16_encode(flag)
enc = ""
for i, c in enumerate(b16):
	enc += shift(c, key[i % len(key)])
print(enc)



def decode(encryption):
	decode = ""
	for i in range(0, len(encryption), 2):
		binary = "{0:04b}".format(ALPHABET.index(encryption[i])) + "{0:04b}".format(ALPHABET.index(encryption[i+1]))
		decode += chr(int(binary, 2))
	return decode



input = "lkmjkemjmkiekeijiiigljlhilihliikiliginliljimiklligljiflhiniiiniiihlhilimlhijil"

for k in ALPHABET:
	flag = ""
	for c in input:
		flag += shift(c, k)
	print(decode(flag))


#result of the readable = et_tu?_431db62c5618cd75f1d0b83832b67b46