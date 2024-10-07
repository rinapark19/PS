while True: # 인풋의 개수가 정해지지 않았을 때 계속 인풋 받기(try - except 구문으로 처리할 것)
    try:
        n = int(input())
    except Exception:
        break
    
    num = 0 # 1로만 이루어진 n의 배수
    i = 1 # 그때 1의 개수
    while True:
        num = num * 10 + 1 # 처음에는 어차피 1임
        num %= n # n으로 나머지 연산해서 나머지가 0이면 1인 배수를 구한 것(그때의 개수가 i)

        if num == 0:
            print(i)
            break
        else:
            i += 1