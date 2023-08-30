import random
lower_case_char="abcdefghijklmnopqrstuvwxyz"
upper_case_char="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="1234567890"
symbols="!@()_-+=/?.>,<:;"

string= upper_case_char+lower_case_char+numbers+symbols
length_of_password=8
password="".join(random.sample(string,length_of_password))

print("Your randomly generated password is: " +password)
