
def is_prime(n):
    if n < 2:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True


def main():
    limit = 100000
    count = 0

    for i in range(2, limit + 1):
        if is_prime(i):
            count += 1

    print("Primes found:", count)


if __name__ == "__main__":
    main()
