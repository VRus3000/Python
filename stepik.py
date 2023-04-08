
print(i_love_none:=[None]*50)

# n = int(input())
# ar = []
# for i in range(n+1):
#     ar.append([1]+[0]*n)

# for i in range(1, n+1):
#     for j in range(1, i+1):
#         ar[i][j] = ar [i-1][j-1]+ ar[i-1][j]

# print(ar)

# n, m = map(int,input().split())
# ar = [max(row:=list(map(int, input().split()))) for _ in range(n)]
# print(ar.count(max(ar)))

# n, m = map(int,input().split())
# ar = [list(map(int, input().split())) for _ in range(n)]
# maxv, maxr, maxc = 0,0,0
# for i in range(n):
#     for j in range(m):
#         if ar[i][j] > maxv:
#             maxv, maxr, maxc = ar[i][j], i, j
# print(maxv)
# print(maxr, maxc)

# m, y, w, x = [sorted([*map(int,input().split())]) for i in range(4)]

# m, n = map(int,input().split())
# a, b = [[int(i) for i in input().split()] for _ in '..']
# res = []
# i, j = 0, 0
# while i < m:
#     while j < n and b[j] <= a[i]:
#         res.append(b[j])
#         j += 1
#     res.append(a[i])
#     i += 1
# res = res + b[j:]
# print(*res)
