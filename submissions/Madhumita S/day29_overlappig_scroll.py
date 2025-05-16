l1 = list(map(int,input("Enter first list: ").split()))
l2 = list(map(int,input("Enter second list: ").split()))
l = []
for i in l1:
    for j in l2:
        if i==j and i not in l:
            l.append(i)
if l:
    print("Common elements: ",end='')
    [print(i,end=' ') for i in l]
else:
    print("No common elements found!")