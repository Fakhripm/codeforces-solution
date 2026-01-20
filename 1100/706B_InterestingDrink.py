n = int(input())
shop = list(map(int, input().split()))
shop.sort()
day = int(input())
for _ in range(day) :
    coin = int(input())
    
    l = 0
    r = n -1
    ans = -1

    while l <= r :
        mid = (l + r) // 2
        
        if shop[mid] <= coin:
            ans = mid
            l = mid + 1 
        else:
            r = mid - 1  
    
    print(ans + 1)