n = int(input())
magnet = input()
group = 1
for i in range(n-1) :
    new_magnet = input()
    if new_magnet != magnet :
        group += 1
        magnet = new_magnet

print(group)