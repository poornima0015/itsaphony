l=[]
n=int(input("enter no"))
a=int(input("enter 2nd no"))
i=1
while(i<=n):
    x=int(input())
    l.append(x)
    i=i+1

def print_big_enough(z,q):
    for j in range(len(z)):
        if(z[j]>=q):
         print(z[j])
print_big_enough(l,a)   
