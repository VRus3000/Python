n, m = map(int,input().split())
ar = [sum(map(int, input().split())) for _ in range(n)]
print(max(ar), ar.index(max(ar)), sep='\n')




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

# '''
