import random

# 選定質數p和原根g
p = 23
g = 5

# 用戶A生成私鑰a
a = random.randint(1, p-1) # a is secret
A = pow(g, a, p) # A = g^a mod p -> send to B

# 用戶B生成私鑰b
b = random.randint(1, p-1) # b is secret
B = pow(g, b, p) # B = g^b mod p -> send to A

# 在公共通道上交換A和B

# 用戶A計算共享密鑰
shared_key_A = pow(B, a, p) # s = B^a mod p

# 用戶B計算共享密鑰
shared_key_B = pow(A, b, p) # s = A^b mod p

assert shared_key_A == shared_key_B
print("共享密鑰:", shared_key_A)

