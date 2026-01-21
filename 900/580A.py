# author : Fakhripm
# problem : KefaandFirstSteps
n = int(input())
seq = list(map(int, input().split()))

current = 1
best = 1

for i in range(n-1) :
    if seq[i+1] >= seq[i] :
        current += 1
    else :
        current = 1
    best = max(current, best)
        

print(best)
