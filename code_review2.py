def is_prime(n):#25
    if n <= 1:
        return False
    elif n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def next_prime(num):
    prime = num + 1
    while not is_prime(prime):
        prime += 1
    return prime

def main():
    num = 10
    print("Is", num, "a prime number?", is_prime(num))
    print("The next prime number after", num, "is", next_prime(num))
    print("Is 17 a prime number?", is_prime(17))
    print("The next prime number after 17 is", next_prime(17))
    print("Is 25 a prime number?", is_prime(25))

if __name__ == "__main__":
    main()
