import math

solution = []
def isPP(n):
    if n <= 1:
        return None
    max_exponent = int(math.log2(n))

    for base in range(2, int(math.sqrt(n)) + 1):
        for exponent in range(2, max_exponent +1):
            result = base ** exponent
            if result == n:
                return [base, exponent]
            elif result > n:
                break
    return None


print(isPP(9))