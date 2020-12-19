import time

def digits(n):
    return (de1(n), de0(n))

def de0(n):
    return int(n % 10)

def de1(n):
    return int(n/10 % 10)

def mult_part(a,b):
    return (de0(a[1]*b[0] + b[1]*a[0] + de1(a[1]*b[1])), de0(a[1]*b[1]))

def pow_digits(n, k):
    n = n % 100 if n > 100 else n
    k = k % 100 if k > 100 else k

    if k < 3:
        return digits(pow(n,k))

    t = mult_part(pow_digits(n, k/2), pow_digits(n, k/2))
    return mult_part(digits(n), t) if k % 2 else t

for i in range(12000, 16000):
    start0 = time.time() * 1000
    v0 = digits(pow(i, i))
    end0 = time.time() * 1000

    start1 = time.time() * 1000
    v1 = pow_digits(i, i)
    end1 = time.time() * 1000

    print('[ok]' if v0 == v1 else '[!!]', i, v0, "--- %.2f ms ---" % (end0-start0), v1, "--- %.2f ms ---" % (end1-start1))
