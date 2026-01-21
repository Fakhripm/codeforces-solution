# author : Fakhripm
# problem : StringTask
word = input().lower()
vowels = set('aeiouy')

result = []
for char in word:
    if char not in vowels:
        result.append('.' + char)

print(''.join(result))
