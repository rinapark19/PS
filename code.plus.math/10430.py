a, b, c = map(int, input().split())

l1 = (a + b) % c
l2 = ((a % c) + (b % c)) % c
l3 = (a * b) % c
l4 = ((a % c) * (b % c)) % c

print(l1)
print(l2)
print(l3)
print(l4)