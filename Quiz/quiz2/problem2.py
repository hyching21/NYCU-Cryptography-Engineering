import hashlib
import time
   
def calculate_speed(data,algo):
    start_time = time.time()
    hash_object = hashlib.new(algo)
    hash_object.update(data)
    hash_object.hexdigest()
    end_time =time.time()
    return end_time - start_time

# open file
with open ("video.mp4",'rb') as f:
    data = f.read()

#calculate speed
algorithms = ["md5","sha1","sha224","sha256","sha512","sha3-224","sha3-256","sha3-512"]
speeds = {}

for algo in algorithms:
    speed = calculate_speed(data,algo)
    speeds[algo] = speed
    
#sort
sorted_algorithms = sorted(algorithms, key=lambda x: speeds[x])
for algo in sorted_algorithms:
    speed = speeds[algo]
    print(f"{algo}'s taken time: {speed}")


