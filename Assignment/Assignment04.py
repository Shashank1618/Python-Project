def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_divisors(n):
    """Return the sum of divisors of a number."""
    return sum(i for i in range(1, n) if n % i == 0)

def is_friendly(n, m):
    """Check if two numbers are friendly."""
    return sum_of_divisors(n) == m and sum_of_divisors(m) == n

def is_kaprekar(n):
    """Check if a number is a Kaprekar number."""
    if n < 1:
        return False
    sqr = n ** 2
    str_sqr = str(sqr)
    d = len(str(n))
    right_part = str_sqr[-d:]
    left_part = str_sqr[:-d] if str_sqr[:-d] else "0"
    return n == int(left_part) + int(right_part)

def is_perfect(n):
    """Check if a number is a perfect number."""
    return sum_of_divisors(n) == n

def find_friendly_pair(n):
    """Find the friendly pair of a given number."""
    for i in range(1, 10000):  # arbitrary limit for search
        if is_friendly(n, i):
            return i
    return None

# Example usage
num = 28
print(f"Is {num} prime? {is_prime(num)}")
print(f"Is {num} Kaprekar? {is_kaprekar(num)}")
print(f"Is {num} perfect? {is_perfect(num)}")
friendly_pair = find_friendly_pair(num)
print(f"The friendly pair of {num} is {friendly_pair}" if friendly_pair else f"No friendly pair found for {num}")
