# author : fakhripm
# problem : 318A - Even Odds

inp1, inp2 = map(int, input().split())

if inp2 > (inp1 + 1) // 2:
    print(2 * (inp2 - (inp1 + 1) // 2))
else:
    print(2 * inp2 - 1)
