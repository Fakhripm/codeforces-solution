m, n = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()
ans = float('inf')
for i in range(n - m + 1):
    diff = arr[i + m - 1] - arr[i]
    if diff < ans:
        ans = diff

print(ans)