def partition(a,p,r):
    x=a[r]
    i=p-1
    for j in range(p,r):
        if a[j]<=x:
            i+=1 
            a[i],a[j]=a[j],a[i]
    a[i+1],a[r]=a[r],a[i+1]
    return i+1 
def quicksort(a,p,r):
    if p<r:
        q=partition(a,p,r)
        quicksort(a,p,q-1)
        quicksort(a,q+1,r)
a=[int(x) for x in input('Enter elements: ').split()]
quicksort(a,0,len(a)-1)
print('sorted array: ',end='')
for i in range(len(a)):
    print('%d'%(a[i]),end=' ')