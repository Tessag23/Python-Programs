a=[int(x) for x in input('enter list elements: ').split()]
for j in range(1,len(a)):
    key=a[j]
    i=j-1
    while i>=0 and a[i]>key:
        a[i+1]=a[i]
        i=i-1
    a[i+1]=key
    print('pass {}: {}'.format(j,a))
print('sorted array: {}'.format(a))