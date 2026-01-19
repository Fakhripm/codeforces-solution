n = int(input())

sum = 0
for x in map(int, input().split()):
    sum += x

print(sum/n)