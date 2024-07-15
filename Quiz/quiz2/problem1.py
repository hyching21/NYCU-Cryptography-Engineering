import hashlib
import time

# read in password list
password_list = []
with open("password.txt",'r') as file:
    for line in file.readlines():
        password_list.append(line.strip())

# crack hash
def crack_hash(hash, password_list):
    start_time = time.time()
    attempts = 0
    for password in password_list:
        attempts += 1
        # convert string to bit, binary to hex
        hashed_password = hashlib.sha1(password.encode()).hexdigest()
        if hashed_password == hash:
            end_time = time.time()
            time_taken = end_time - start_time
            return password, attempts ,time_taken
    return None, attempts, None

# for question c. hash + salt
def crack_salthash(hash, password_list, salt):
    start_time = time.time()
    attempts = 0
    for password in password_list:
        attempts += 1
        # convert string to bit, binary to hex
        concatenated_str = salt + password
        hashed_password = hashlib.sha1(concatenated_str.encode()).hexdigest()
        if hashed_password == hash:
            end_time = time.time()
            time_taken = end_time - start_time
            return password, attempts ,time_taken
    return None, attempts, None

def print_ans(hash, password, attempts, time_taken):
    
    if password :
        print("Hash: "+ hash ) 
        print("Password: " + password) 
        #time_taken_formatted = str(datetime.timedelta(seconds=time_taken))
        time_taken_formatted = "{:02}:{:02}:{:09.6f}".format(int(time_taken // 3600),int((time_taken % 3600) // 60),time_taken % 60)
        print(f"Took {attempts} attempts to crack input hash. Time Taken: {time_taken_formatted}\n")
    else:
        print("Failed to crack hash.\n")

#main 

#input
hash1 = "ef0ebbb77298e1fbd81f756a4efc35b977c93dae"
hash2 = "0bc2f4f2e1f8944866c2e952a5b59acabd1cebf2"
hash3 = "9d6b628c1f81b4795c0266c0f12123c1e09a7ad3"
salt = "dfc3e4f0b9b5fb047e9be9fb89016f290d2abb06"

password_1, attempts_1 ,time_taken_1 = crack_hash(hash1 , password_list)
password_2, attempts_2 ,time_taken_2 = crack_hash(hash2 , password_list)
salt_str, attempts_salt ,time_taken_salt = crack_hash(salt , password_list)
password_3, attempts_3 ,time_taken_3 = crack_salthash(hash3 , password_list, salt_str)

print_ans(hash1,password_1, attempts_1 ,time_taken_1)
print_ans(hash2,password_2, attempts_2 ,time_taken_2)
print_ans(hash3,password_3, attempts_salt+attempts_3 ,time_taken_3+time_taken_salt)


