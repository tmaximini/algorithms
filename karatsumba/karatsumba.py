# we want to implement a large integer multiplication more efficiently using divide and conquer and recursion
def karat(x, y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y
    else:
        n = max(len(str(x)), len(str(y)))
        n_half = n // 2 # use explicit floor division operator //

        # zero pad with half length
        a = x // (10 ** n_half) 
        b = x % (10 ** n_half)
        c = y // (10 ** n_half)
        d = y % (10 ** n_half)

        # recursively calculate partials
        z0 = karat(b,d)
        z1 = karat((a+b),(c+d))
        z2 = karat(a,c)

        return (z2 * (10 ** (n_half * 2))) + ((z1 - z2 - z0) * (10 ** n_half)) + z0



print(karat(10000, 10000))