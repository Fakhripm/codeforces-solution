# author : Fakhripm
# problem : QueueAtTheSchool
n, t = map(int, input().split())
queue = input()

queue = list(queue)

while t > 0:
    i = 0
    while i < n - 1:
        if queue[i] == 'B' and queue[i + 1] == 'G':
            queue[i], queue[i + 1] = 'G', 'B'
            i += 2   
        else:
            i += 1
    t -= 1

queue = ''.join(queue)
print(queue)
