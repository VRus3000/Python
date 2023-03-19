import math
M = int(input())
a = [[0] * M for i in range(M)]
n,i,j = 1, 0, -1
# n - само число
# d - индекс текущего направления
# x,y - координаты заполняемой ячейки

'''
V = [0,1,0,-1]  # матрица направлений
for d in range(1,2*M):
    for _ in range(M-d//2):
        j += V[d%4]    
        i += V[(d-1)%4]
        a[i][j] = n
        n += 1
'''
for d in range(1, 2*M):
    for _ in range(M-d//2):
        j += int (math.sin(d%4*math.pi/2))    # Сдвигаемся к следующей ячейке
        i -= int (math.cos(d%4*math.pi/2))
        a[i][j] = n
        n += 1

'''
i, j, di, dj = 0, 0, 0, 1
for n in range(1, M*M+1):
    a[i][j] = n
    if a[(i+di)%M][(j+dj)%M]:
        di, dj = dj, -di
    i, j = i + di, j + dj
'''    
[print(*i) for i in a]

