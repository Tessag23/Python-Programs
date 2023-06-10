l=[int(x) for x in input('enter list elements: ').split()]
s=int(input('enter search element: '))
low=0
high=len(l)-1
f=0
while(low<=high):
    mid=(high+low)//2
    if l[mid]==s:
        print('%d found at index %d'%(s,mid))
        f=1
        break
    elif l[mid]>s:
        high=mid-1
    else:
        low=mid+1
if f==0:
    print('%d not found'%(s))