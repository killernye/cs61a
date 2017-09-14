def  split(n):
    """Split positive numbers into all but its last digit and its last digit."""
    return n // 10, n % 10

def sum_digits(n):
    """Return the sum of the digits of positive integer n."""
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
    return last + sum_digits(all_but_last)


def sum_digits_iter(n):
    digit_sum = 0
    while n > 0:
        n, last = split(n)
        digit_sum += last
    return digit_sum


def sum_digits_recur(n, digit_sum):
    if n == 0:
        return digit_sum
    else:
        n, last = split(n)
        return sum_digits_recur(n, digit_sum + last)

def recur_fibo(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return recur_fibo(n-1) + recur_fibo(n-2)

def luhn_sum_iter(n):
    sum = 0
    double = False
    while n > 0:
        last_digit = n % 10
        if double:
            last_digit *= 2
            last_digit = last_digit % 10 +  last_digit // 10
        sum, n, double = sum + last_digit, n // 10, not double
    return sum


def luhn_sum(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return last + luhn_sum_double(all_but_last)

def luhn_sum_double(n):
    if n < 10:
        return sum(split(n * 2))
    else:
        all_but_last, last = split(n)
        return sum(split(2 * last)) + luhn_sum(all_but_last)
