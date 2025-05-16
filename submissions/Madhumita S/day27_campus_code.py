l = list(map(int,input("Enter module scores (space-separated): ").split()))
d = [i for i in l if i<50]
if d==[]:
    print("All modules are working fine!")
else:
    print("Modules to debug: ",end='')
    for i in d: print(i,end=' ')