#Дано целое число N (>0). Найти сумму N^2 + (N + 1)^2 + (N + 2)^2 + ... + (2 * N)^2
N = int(input('Введите целое число N: '))
m = 0
for i in range(N, 2 * N + 1):
    m = m + i ** 2
print(m)