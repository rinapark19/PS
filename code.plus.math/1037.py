num = int(input())

n_li = list(map(int, input().split()))

n1 = min(n_li)
n2 = max(n_li)

print(n1 * n2)