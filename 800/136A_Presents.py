n = int(input())
gifts = list(map(int, input().split()))
receive = [0] * n
for i, gift in enumerate(gifts):
    receive[gift - 1] = i + 1

for rec in receive :
    print(rec)