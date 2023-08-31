n= int(input())

for i in range(1,n+1):
    if i==1:
        print(int(n)*"*")
    elif i==n:
        print(int(n) * "*")
    else:
        print("*"+int(n-2)*" "+"*")