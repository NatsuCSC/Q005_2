H, W = map(int, input().split())
A = [[*input()] for _ in range(H)]
B = [[*input()] for _ in range(H)]

if sum(A, []).count('@') == sum(B,[]).count('@'):
    print('Yes')
else:
    print('No')
