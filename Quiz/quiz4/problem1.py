a = [[0] * 8 for _ in range(550)]
for i in range(0,550):
    ans = ""
    degree = [0]*8
    if 0 <= i <= 7 :
        degree[i] = 1
        a[i] = degree

    else:
        for j in range(0,8):
            a[i][j]=(a[i-4][j]+a[i-5][j]+a[i-6][j]+a[i-8][j])%2

    for j in range(0,8):
        if(a[i][j]==1):
            ans+=(f"x^{j} ") 

    print(f"a^{i} = {ans}")
    
print('\n')    
## non-primitive example:
    
a = [[0] * 8 for _ in range(300)]
for i in range(0,300):
    ans = ""
    degree = [0]*8
    if 0 <= i <= 7 :
        degree[i] = 1
        a[i] = degree

    else:
        for j in range(0,8):
            a[i][j]=(a[i-4][j]+a[i-5][j]+a[i-7][j]+a[i-8][j])%2

    for j in range(0,8):
        if(a[i][j]==1):
            ans+=(f"x^{j} ") 

    print(f"a^{i} = {ans}")