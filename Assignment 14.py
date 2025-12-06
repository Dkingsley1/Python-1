def power(base, exponent):
    # Handle exponent 0
    if exponent == 0:
        return 1

    # If exponent is negative, compute positive exponent and invert
    if exponent < 0:
        return 1 / power(base, -exponent)

    # Fast exponentiation (binary exponentiation)
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:  # If exponent is odd
            result *= base
        base *= base
        exponent //= 2
    return result
