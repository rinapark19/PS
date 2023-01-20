import sys
word = list(input())
answer = []
tmp = []

for i in range(1, len(word) - 1):
    for j in range(i+1, len(word)):
        a = word[:i]
        b = word[i:j]
        c = word[j:]
        a.reverse()
        b.reverse()
        c.reverse()
        tmp.append(a + b + c)

for a in tmp:
    answer.append(''.join(a))

print(sorted(answer)[0])

# 직접 하면 안 됨
# brute force로 하나하나 다 해 봐야 함
# 단어마다 접근 방법이 달라서 다 해 보는 방법밖에 없다
