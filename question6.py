def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True


count = 0
num = 2

print("Getting you the 10001 th prime number. It may take upto 1min, Please be paitent.")
while count < 10001:
    count += 1 if is_prime(num) else 0
    num += 1

print(f"The 10001th prime number is {num - 1}")