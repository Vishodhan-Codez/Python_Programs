import random

def generate_password(length=12): # all letters in password
    n = input("Do you want symbols ? (y/n)")
    if n == "y" :
        symbols = '!@#$%^&*([{|\"":;/?.><,~`=+-_}])!@#$%^&*([{|\"":;/?.><,~`=+-_}])!@#$%^&*([{|\"":;/?.><,~`=+-_}])!@#$%^&*([{|\"":;/?.><,~`=+-_}])!@#$%^&*([{|\"":;/?.><,~`=+-_}])'
    else :
        symbols = 'a'
    lower_case = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890'
    all_characters = lower_case + upper_case + numbers + symbols
    password = [
        random.choice(lower_case),
        random.choice(upper_case),
        random.choice(numbers)
    ]
    while len(password) < length:
        password.append(random.choice(all_characters))
    random.shuffle(password)
    return ''.join(password)
for i in range(1,11,1) :
    print("Random Password:", generate_password())