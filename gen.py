import string
import itertools

def f():
    yield 1
    yield 5
    yield 7

g = f()
print(g)

for x in g:
    print(x)

def letters():
    for c in string.ascii_lowercase:
        yield c

for letter in letters():
    print(letter)

def primes():
    yield 2
    prime_cache = [2]
    for n in itertools.count(3, 2):
        is_prime = True
        for p in prime_cache:
            if n % p == 0:
                is_prime = False
                break
        if is_prime:
            prime_cache.append(n)
            yield n

for p in primes():
    print(p)
    if p > 100_000:
        break

# generator, not list comprehension, because
# enclosed in () not []
squares = ( x*x for x in itertools.count(1) )

for x in squares:
    print(x)
    if x > 1_000:
        squares.close()




