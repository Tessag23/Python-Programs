def merge(a,p,q,r):
    n1=q-p+1
    n2=r-q
    L,R=[],[]
    for i in range(n1):
        L.append(a[p+i])
    for j in range(n2):
        R.append(a[q+j+1])
    L.append(1000000)
    R.append(1000000)
    i=j=0 
    for k in range(p,r+1):
        if L[i]<=R[j]:
            a[k]=L[i]
            i+=1
        else:
            a[k]=R[j]
            j+=1 
def mergesort(a,p,r):
    if p<r:
        q=((p+r)//2)
        mergesort(a,p,q)
        mergesort(a,q+1,r)
        merge(a,p,q,r)
a=[int(x) for x in input('enter elements: ').split()]
mergesort(a,0,len(a)-1)
print('sorted array: {}'.format(a))