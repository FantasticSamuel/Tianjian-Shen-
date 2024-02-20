#沈天健 2300011417
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(sum):
    for i in range(2, sum):
        if is_prime(i) and is_prime(sum - i):
            return i, sum - i

sum = int(input().strip())
a, b = find_primes(sum)
print(a, b)