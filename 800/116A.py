# author : Fakhripm
# problem : Tram
n = int(input())
current = 0
max_passengers = 0
for i in range(n):
    a, b = map(int, input().split())
    current = current - a + b
    if current > max_passengers:
        max_passengers = current
print(max_passengers)
