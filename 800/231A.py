# author : Fakhripm
# problem : Team
loop = int(input())
count = 0
for i in range(loop):
    inp1, inp2, inp3 = map(int, input().split())
    if inp1 + inp2 + inp3 >= 2:
        count += 1
print(count)
