#Дано целое число N (>0). Найти сумму 1 + 1/2 + 1/3 + ... + 1/N
N = int(input('Введите целое число N: '))
m = 1
for i in range(1, N):
    m = m + 1/i
print(m)
