# author : Fakhripm
# problem : Is your horseshoe on the other hoof?

unique = set()
for x in map(int, input().split()) :
    unique.add(x)

print(4 - len(unique))