H, W = map(int, input().split())
A = [[*input()] for _ in range(H)]
B = [[*input()] for _ in range(H)]
x = sum(A, [])
y = sum(B, [])

if x.count('@') == y.count('@'):
    print('Yes')
else:
    print('No')
