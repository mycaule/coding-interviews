### Usage

Small program that computes the two first digits of the big number n^n.

```
$ python main.py
```

### Explanation

Let's define the two last digits of a integer *n* as:

```
digits(n) = (d1(n), d0(n))
d1(n) = n/10 % 10
d0(n) = n % 10
```

The multiplication algorithm taught at school for two integer gives this recursive formula:
```
digits(a.b) = digits(10.d0(a).d1(b) + 10.d0(b).d1(a) + d0(a).d0(b))
            = (d0(d0(a).d1(b) + d0(b).d1(a) + d1(d0(a).d0(b))), d0(d0(a).d0(b)))
            = f(a, b)
```

```
if n = 2k
  digits(n^n) = digits(n^k.n^k)
              = f(n^k, n^k)

if n = 2k+1
  digits(n^n) = digits(n.n^k.n^k)
              = f(n, n^k.n^k)
              = f(n, f(n^k, n^k))
```

Also note that *Z/100Z* preserve multiplication and hence let *0 <= p < 100* where *n = p [100]*,
*n^n = p^n [100]*

We observe that the sequence of number we produced in periodic resulting from Carmichael and Fermat little theorem, which is a path to improve the algorithm a little more.

### Reference

[Last two digits of n^n periodicity](https://math.stackexchange.com/questions/2733502/last-two-digits-of-nn-periodicity)
