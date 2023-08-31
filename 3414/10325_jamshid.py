a, b =map(int, input().split())

radif =11-a

if b<=10:
        seton = b
        print("Right", radif , seton)
else:
        seton = 21-b
        print("Left", radif, seton)