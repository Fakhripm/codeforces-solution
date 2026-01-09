# Author: fakhripm
# Problem: 263A - Beautiful Matrix

for i in range(5):
    row = list(map(int, input().split()))
    if 1 in row:
        x = i
        y = row.index(1)

if x > 2:
    x_moves = x - 2
else:
    x_moves = 2 - x 

if y > 2:
    y_moves = y - 2
else:
    y_moves = 2 - y 
print(x_moves + y_moves)
