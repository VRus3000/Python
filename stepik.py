s = input()
st = ['-']
for c in s:
    if c in '([{':
        st.append(c)
    else:
        if st[-1] + c in ['()','[]','{}']:
            st.pop()
        else:
            print('NO')
            break
else:
    print('YES' if st == ['-'] else 'NO')

'''

4
1 2 3 4 5
3 
7 9 4 2 8

m, y, w, x = [sorted([*map(int,input().split())]) for i in range(4)]

m, n = map(int,input().split())
a, b = [[int(i) for i in input().split()] for _ in '..']
res = []
i, j = 0, 0
while i < m:
    while j < n and b[j] <= a[i]:
        res.append(b[j])
        j += 1
    res.append(a[i])
    i += 1
res = res + b[j:]
print(*res)

'''
