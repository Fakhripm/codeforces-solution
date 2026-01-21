# problem : Lucky Division

n = int(input())

result = []
queue = [4, 7]  
index = 0       

while index < len(queue):
    num = queue[index]
    index += 1  
    if num > n:
        continue

    result.append(num)

    queue.append(num * 10 + 4)
    queue.append(num * 10 + 7)

for item in result :
    if n%item == 0 :
        print("YES")
        exit()

print("NO")