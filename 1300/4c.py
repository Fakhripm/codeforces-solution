# author : Fakhripm
# problem : RegistrationSystem
n = int(input())
username = {}
for _ in range(n) :
    x = input()
    if x not in username :
        print("OK")
        username[x] = 1
    else :
        print(x + str(username[x]))
        username[x] += 1
        
