# author : fakhripm
# problem : 1030A - In Search of an Easy Problem

n = int(input())
a = map(int, input().split())

total = sum((a))
if total == 0 :
    print("EASY")
else : 
    print("HARD")