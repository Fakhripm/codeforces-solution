# author : Fakhripm
# problem : InSearchofAnEasyProblem
n = int(input())
a = map(int, input().split())

total = sum((a))
if total == 0 :
    print("EASY")
else : 
    print("HARD")
