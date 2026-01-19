n = int(input())

count1 = 0
count2 = 0
count3 = 0
count4 = 0
for x in map(int, input().split()):
    if x == 1:
        count1 += 1
    elif x == 2:
        count2 += 1
    elif x == 3:
        count3 += 1
    else:
        count4 += 1

taxi = 0
taxi += count4

taxi += count3
count1 = max(0, count1 - count3)

taxi += count2 // 2
if count2 % 2 == 1:
    taxi += 1
    count1 = max(0, count1 - 2)

taxi += (count1 + 3) // 4
print(taxi)