digit = int(input())
first = digit // 100
second = (digit // 10) % 10
third = digit % 10
print(first + second + third)
