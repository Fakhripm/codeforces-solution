# author : Fakhripm
# problem : Twins
val= int(input())
coins = list(map(int, input().split()))

total = sum(coins)
coins.sort(reverse=True)
count = 0
you = 0
for coin in coins:
    you += coin
    total -= coin
    count += 1
    if you > total:
        print(count)
        break
