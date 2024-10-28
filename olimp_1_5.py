import math

n = int(input(f'Введите число: '))

m = 2 * n

delta = 1 + 8 * n
sqrt_delta = int(math.isqrt(delta))

if sqrt_delta * sqrt_delta < delta:
    sqrt_delta += 1

k_max = (sqrt_delta - 1) // 2


count = 0

for k in range(1, k_max + 1):
    if m % k == 0:
        temp = (m // k) - k + 1
        if temp % 2 == 0:
            a = temp // 2
            if a >= 1:
                count += 1


print(f'Количество представлений: {count}')