# author : Fakhripm
# problem : SoldierAndBanana
k, n, w = map(int, input().split())
total_cost = k * w * (w + 1)  // 2
borrow = total_cost - n
print(borrow if borrow > 0 else 0)
