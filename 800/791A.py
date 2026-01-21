# author : Fakhripm
# problem : BearAndBigBrother
inp1, inp2 = map(int, input().split())
count = 0
while inp1 <= inp2:
    inp1 *= 3
    inp2 *= 2
    count += 1
print(count)
