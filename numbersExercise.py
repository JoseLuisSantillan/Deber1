from string import ascii_uppercase as uppercase

array = [16, 9, 3, 15, 3, 20, 6, 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14]


flag = []
for index in array:
    print(uppercase[index-1])
    flag.append(uppercase[index-1])
print("".join(flag))