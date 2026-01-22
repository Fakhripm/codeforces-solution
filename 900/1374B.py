# problem : Multiply by 2, divide by 6

n = int(input()) 
for _ in range(n) :
    c2 = 0
    c3 = 0
    x = int(input())
    x2 = x
    x3 = x
    while x2%2 == 0 :
        x2 //= 2
        c2 += 1
    while x3%3 == 0 :
        x3 //= 3
        c3 += 1
    while x%2 == 0 :
        x //= 2
    while x%3 == 0 :
        x //= 3
    if x == 1 :
        if c2 > c3 :
            print(-1)
        else :
            print(c2 + 2 * (c3 - c2))
    else : print(-1)