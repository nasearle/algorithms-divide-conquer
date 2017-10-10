from math import log10

def multiply(x, y):
    reduce = False
    if x == 0 or y == 0:
        return 0
    if x < 10 and y < 10:
        return x * y
    else:
        if x < 10:
            x *= 10
            reduce = True
        if y < 10:
            y *= 10
            reduce = True

        x_length = int(log10(x)) + 1
        y_length = int(log10(y)) + 1
        mid = min(x_length/2, y_length/2)
        shift = 10**mid

        a = x / shift
        b = x % shift
        c = y / shift
        d = y % shift

        add1 = a + b
        add2 = c + d
        var1 = multiply(a, c)
        var2 = multiply(b, d)
        var3 = multiply(add1, add2)
        # var3 = multiply(a, d)
        # var4 = multiply(b, c)

        result = shift**2 * var1 + shift * (var3 - var1 - var2) + var2
        if reduce:
            return result / 10
        return result

actual = multiply(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627)
expected = 2718281828459045235360287471352662497757247093699959574966967627 * 3141592653589793238462643383279502884197169399375105820974944592

print actual
print actual == expected
