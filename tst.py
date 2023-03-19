

    
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
