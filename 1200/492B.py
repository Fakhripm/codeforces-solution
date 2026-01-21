# author : Fakhripm
# problem : VanyaandLanterns
n, l  = map(int, input().split())
lanterns = list(map(int, input().split()))
lanterns.sort()

max_gap = max(lanterns[0] - 0, l - lanterns[-1])
for i in range(1, n):
    gap = (lanterns[i] - lanterns[i - 1]) / 2
    if gap > max_gap:
        max_gap = gap  

print(max_gap)
