n= input()

def to_lower(char: str):
    if 'Z' >= char >= 'A':
       return "_"+char.lower()
    else:
        return char

word =[]
for i in n:
    word.append(to_lower(i))

if word[0][0]=='_':
    word[0]=word[0][1]

print("".join(word))



