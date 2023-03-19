with open('advent_3.test') as f:
    N, H = map(int, f.readline().rstrip().split())
    arr = list(map(int, f.readline().rstrip().split()))

arr.sort(reverse=True)

slen = 0
for i in range(N):
    slen = slen + arr[i]
    if slen >= H:
        break

print(f'Num of knots is {i}, length of rope is {slen}')
