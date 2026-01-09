# Author: fakhripm
# Problem: 158A - Next Round

inp1, inp2 = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
for j in range(inp1):
    if arr[j] >= arr[inp2-1] and arr[j] > 0:
        count += 1
print(count)