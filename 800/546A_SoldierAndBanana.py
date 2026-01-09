# author : fakhripm
# problem : 546A - Soldier and Bananas

k, n, w = map(int, input().split())
total_cost = k * w * (w + 1)  // 2
borrow = total_cost - n
print(borrow if borrow > 0 else 0)