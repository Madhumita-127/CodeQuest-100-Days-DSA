l=input("Enter a sentence: ").split()
long = l[0]
for i in l:
    if len(i)>len(long):
        long = i
print("Longest word:",long)