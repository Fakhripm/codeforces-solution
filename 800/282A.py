# author : Fakhripm
# problem : Bit++
x = 0
inp = int(input())
for i in range(0, inp ):
    y = input()
    if y == "++X" or y == "X++":
        x += 1
    else:
        x -= 1
print(x)
