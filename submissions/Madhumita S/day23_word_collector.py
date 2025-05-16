s = list(input("Enter text: ").lower().split())
l = []
for i in s:
    k=''
    for j in i:
        if j.isalnum(): k = k + j
    if k : l.append(k)
q = set(l)
for i in q:
    print(i,':',l.count(i))