
#include <stdio.h>

int is_prime(int n) {
    if (n < 2) {
        return 0;
    }

    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            return 0;
        }
    }

    return 1;
}

int main() {
    int limit = 100000;
    int count = 0;

    for (int i = 2; i <= limit; i++) {
        if (is_prime(i)) {
            count++;
        }
    }

    printf("Primes found: %d\n", count);

    return 0;
}