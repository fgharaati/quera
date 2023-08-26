n=int(input())

lis=[]

while n!=0:
    lis.append(n)
    n=int(input())
lis.reverse()

for i in lis:
    print(i)


