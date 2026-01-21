# author : Fakhripm
# problem : AntonAndDanik
n = int(input())
matches = input()

anton_wins = matches.count('A')
danik_wins = matches.count('D')
if anton_wins > danik_wins:
    print("Anton")
elif danik_wins > anton_wins:
    print("Danik")
else:
    print("Friendship")
