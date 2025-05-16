s = input("Enter cipher text: ")
n = int(input("Enter shift value: "))
print("Decoded Message: ",end='')
l = ''
for i in range(0,len(s)):
    if s[i].isalpha():
        k = ord(s[i]) - n
        if k<65 and s[i].isupper() or k<97 and s[i].islower():
            k = 25 - k
        l = l + chr(k)
    else: l = l + s[i]
print(l)