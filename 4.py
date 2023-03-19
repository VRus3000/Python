with open('advent_4.test.txt') as f:
    N = int(f.readline())
    arr = list(map(int, f.readline().rstrip().split()))


pos = 0
arr2 = arr
for i in range(N):
    arr2 = arr2[1:]+arr2[:1]
    pos += 1
    if arr == arr2:
        break

print(f'{N/pos} повторений с позиции {pos}')
