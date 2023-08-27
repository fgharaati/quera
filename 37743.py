n=int(input())
char=input()
repeat=int(input())
def pattern(n, char, repeat):
    if n%2==0:
        n+=1
    for i in range(repeat):
        for i in range(1, n+1,2):
            space=(n-i)//2
            print(" "*space+i*char)
        for i in range(n-1, 0, -1):
            if i%2!=0:
                space=(n-i)//2
                print(" "*space+i*char)

pattern(n,char, repeat)

