string = input()

resl=[]

def find(char):
    for pair in resl:
        if pair[0] == char:
            return pair
    return False

for char in string:
    pair = find(char)

    if pair == False:
        resl.append([char, 1])
    else:
        pair[1]+=1

for pair in resl:
    print(pair[0], pair[1])
