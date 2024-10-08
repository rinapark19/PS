import sys

def gcd(a, b):
    while b != 0:
        t = a % b
        (a, b) = (b, t)
    return a

m, n = map(int, sys.stdin.readline().split())

gcd_value = gcd(m, n)

print(gcd_value)
print((int(m * n / gcd_value)))
