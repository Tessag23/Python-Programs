l=[int(x) for x in input('enter list elements: ').split()]
s=int(input("enter search element: "))
f=0
for i in range(len(l)):
    if s==l[i]:
        f=1
        print(s,"found at index",i) 
        break
if f==0:
    print(s,'not found')