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
    yield 3
    prime_cache = [2, 3]
    square_me = 1
    squared = 1
    for n in itertools.count(5, 2):
        if n == squared:
            is_prime = False
            square_me += 1
            squared = square_me*square_me
        else:
            while n > squared:
                square_me += 1
                squared = square_me*square_me
            
            for p in prime_cache[1:]:
                if n % p == 0:
                    is_prime = False
                    break
                elif p >= square_me:
                    is_prime = True
                    break
        if is_prime:
            prime_cache.append(n)
            yield n

print('list primes')
for p in primes():
    print(p)
    if p > 10_00_000:
        break
print('done listing primes')

# generator, not list comprehension, because
# enclosed in () not []
squares = ( x*x for x in itertools.count(1) )

for x in squares:
    print(x)
    if x > 1_000:
        squares.close()

