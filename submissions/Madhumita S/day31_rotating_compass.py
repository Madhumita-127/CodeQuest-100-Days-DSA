l = list(map(int,input("Enter numbers: ").split()))
k = int(input("Enter rotation value (K): "))
if k>len(l):
    k = k%len(l)
rotated = l[-k:] + l[:-k]
print("Rotated Array: ",end='')
[print(i,end=' ') for i in rotated]