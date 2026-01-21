# author : Fakhripm
# problem : Word

word = input()
upper_count = sum(map(str.isupper, word))

if upper_count > len(word) / 2:
    print(word.upper())  
else:
    print(word.lower())
