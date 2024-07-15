import random

sys_random = random.SystemRandom()
num_bits = 8388608  # 1024 * 1024 * 8 bits = 8388608 bits

random_bits = [sys_random.randint(0, 1) for _ in range(num_bits)]
byte_lists = [random_bits[i:i+8] for i in range(0, len(random_bits), 8)]
random_bytes = bytes([int(''.join(map(str, byte)), 2) for byte in byte_lists])

with open('random.bin', 'wb') as file:
        file.write(random_bytes)

