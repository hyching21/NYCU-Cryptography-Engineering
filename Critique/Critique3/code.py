import random
import hashlib

def generate_key_pairs(n):
    key_pairs = []
    for _ in range(n):
        key_a = random.randint(1, 2**16)
        key_b = hashlib.sha256(str(key_a).encode()).hexdigest()
        key_pairs.append((key_a, key_b))
    return key_pairs

def encrypt_keys(key_pairs):
    encrypted_keys = []
    for key_a, key_b in key_pairs:
        encrypted_key = hashlib.sha256(str(key_a).encode()).hexdigest()
        encrypted_keys.append((encrypted_key, key_b))
    return encrypted_keys

def user_a_phase_1():
    key_pairs = generate_key_pairs(1000)
    encrypted_keys = encrypt_keys(key_pairs)
    return key_pairs, encrypted_keys

def user_b_phase(encrypted_keys):
    chosen_index = random.randint(0, len(encrypted_keys) - 1)
    chosen_key = encrypted_keys[chosen_index][1]
    return chosen_index, chosen_key

def user_a_phase_2(key_pairs, chosen_index):
    chosen_key = key_pairs[chosen_index][1]
    return chosen_key

# 用戶A生成密鑰對和加密密鑰
key_pairs, encrypted_keys = user_a_phase_1()

# 用戶B選擇並解密一個密鑰對
chosen_index, chosen_key_b = user_b_phase(encrypted_keys)
print(f"用戶B選擇的索引: {chosen_index}, 用戶B解密的密鑰: {chosen_key_b}")

# 用戶A確認用戶B選擇的密鑰對
chosen_key_a = user_a_phase_2(key_pairs, chosen_index)
print(f"用戶A確認的密鑰: {chosen_key_a}")

# 驗證雙方獲得相同的密鑰
if chosen_key_a == chosen_key_b:
    print("密鑰交換成功，雙方獲得相同的密鑰:", chosen_key_a)
else:
    print("密鑰交換失敗，雙方獲得不同的密鑰。")
