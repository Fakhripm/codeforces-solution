# problem : Cheap Travel

n, m, a, b = map(int, input().split())

all_single = n * a

full_passes = n // m
remaining = n % m

mixed = full_passes * b + min(remaining * a, b)

print(min(all_single, mixed))