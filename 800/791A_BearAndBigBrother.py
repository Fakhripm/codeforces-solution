# author: fakhripm
# problem: 791A - Bear and Big Brother

inp1, inp2 = map(int, input().split())
count = 0
while inp1 <= inp2:
    inp1 *= 3
    inp2 *= 2
    count += 1
print(count)