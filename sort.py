# Сортировка вставками
i, ar = input(), list(map(int, input().split()))
for i in range (1, len(ar)): 
    j, x = i, ar[i]
    while (j > 0 and ar[j-1] > x): 
        ar[j] = ar[j-1]
        j -= 1
    ar[j] = x
print(*ar)
'''
# Пузырьком
n, m = map(int, input().split())
a, b, c = 0, 0, 0
for a in range(int(n**0.5+1)):
    for b in range(int(m**0.5+1)):
        if a*a+b==n and a+b*b==m:
            c += 1
print(c)
'''
