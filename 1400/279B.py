# author : Fakhripm
# problem : Books
n,t = map(int, input().split())
arrt = list(map(int, input().split()))

res = -1
l = 0
sumt = 0

for r in range(len(arrt)) :
    sumt += arrt[r]
    while sumt > t :
        sumt -= arrt[l]
        l += 1
    
    res = max(r - l + 1, res)
print(res)
