lis=[]

for i in range(4):
    name = input()
    direction = input()

    if direction=="L":
        lis.insert(0,name)
    elif direction=="R":
        lis.append(name)
print(lis[1])


