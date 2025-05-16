s = input("Enter a sentence:")
v = c = 0
for i in s:
    if i.isalpha():
        if i.lower() in "aeiou":
            v += 1
        else:
            c += 1
print("Vowels:",v)
print("Consonants:",c)