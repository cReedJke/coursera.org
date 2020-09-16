A = int(input())
B = int(input())
N = int(input())
kop = B * N % 100
rub = A * N + (B * N // 100)
print(rub, kop)
