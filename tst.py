i = input()
ar, i, j, cnt = list(map(int, input().split())), 0, 0, 0

for i in range(len(ar)-1):
    for j in range(len(ar)-i-1):
        if ar[j] > ar[j+1]:
            ar[j], ar[j+1] = ar[j+1], ar[j]
            cnt += 1
print(*ar)
print(cnt)



    
'''
print('YNEOS'[input() != input()[::-1]::2])

#
string='AHGSYVDIUGGHJ'
k=4
n=len(string)//k

ar=([string[i*k:(i+1)*k] for i in range(n)])
for i in range(n):
    print(''.join(ar[i][j] for j in range(k) if ar[i][j] not in ar[i][:j]))

#
def minion_game(string):
    vow,cons = 0,0
    N = len(string)
    for i in range(N):
        if s[i] in 'AEIOU':
            vow += N-i
        else:
            cons += N-i
    if vow > cons:
        print(f'Kevin {vow}')
    elif vow < cons:
        print(f'Stuart {cons}')
    else:
        print('Draw')
        
    b = set(map(int, input().split()))
    print (*sorted(a ^ b), sep='\n')
'''
