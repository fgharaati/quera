n= input()

digit_numbers=len(n)

Number=int(n)
def tavan_n(Y):
    return Y**digit_numbers

sum=0
for i in n:
    Yekan= Number%10
    res=tavan_n(Yekan)
    sum+=res
    Number//=10

if sum==int(n):
    print("Yes")
else:
    print("No")