number1= int(input())

number2=int(number1)
new_number=0
while number1>0:
    i=number1%10
    number1//=10
    new_number=new_number*10+i

if number2==new_number:
     print("yes")
else:
  print("no")
