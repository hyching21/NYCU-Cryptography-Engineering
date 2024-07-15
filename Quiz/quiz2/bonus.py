# import hashlib
# import time

# read in password list
output_file = "reversed_passwords.txt"
space_file = "space_passwords.txt"
password_list = []
with open("password.txt",'r') as file:
    for line in file.readlines():
        password_list.append(line.strip())

password_list.reverse()

with open(output_file, 'w') as file:
    for password in password_list:
        file.write(password + '\n')

with open(space_file, 'w') as file:
    for password in password_list:
        file.write(" " + password + '\n')

# #main 
# def find_passwords(hash_value, password_list):
#     attempts = 0
#     start_time = time.time()
#     for password1 in password_list:
#         for password2 in password_list:
#             attempts += 1
#             concatenated_passwords = password1 + " " + password2
#             hashed_passwords = hashlib.sha1(concatenated_passwords.encode()).hexdigest()
#             if hashed_passwords == hash_value:
#                 end_time = time.time()
#                 time_taken = end_time - start_time
#                 return password1, password2, attempts, time_taken
#     return None, None, attempts, None  


# #input
# hash = "44ac8049dd677cb5bc0ee2aac622a0f42838b34d"
# password1, password2, attempts, time_taken = find_passwords(hash, password_list)
# #print
# print("Hash: "+ hash ) 
# print("Password: " + password1 + " " + password2) 
# time_taken_formatted = "{:02}:{:02}:{:09.6f}".format(int(time_taken // 3600),int((time_taken % 3600) // 60),time_taken % 60)
# print(f"Took {attempts} attempts to crack input hash. Time Taken: {time_taken_formatted}\n")

