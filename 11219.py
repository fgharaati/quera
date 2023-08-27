n= int(input())
m=int(input())
p=int(input())

lis=[]
for i in range(n+1,m):
    if i%p==0:
       lis.append(i)
       i+=1
print(len(lis))