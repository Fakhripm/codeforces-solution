a_bin = input()
b_bin = input()

a = int(a_bin, 2)
b = int(b_bin, 2)

c = a ^ b

width = max(len(a_bin), len(b_bin))
print(format(c, f'0{width}b'))
