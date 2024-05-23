# fibonacci infinitive

class Fibonacci:
    def __init__(self):
        self._start, self._next = 0, 1
        self._current: int = 0

    def __iter__(self):
        return self

    def __next__(self):
        self._current = self._start
        self._start, self._next = self._next, self._next + self._start
        return self._current


f = Fibonacci()
print(next(f))
print(next(f))
print(next(f))
print(next(f))
# for i in f:
#     print(i)

# fibonacci infinitive with generator


def fibo_infinitive():
    n1, n2 = 0, 1
    while True:
        yield n1
        n1, n2 = n2, n1 + n2


f2 = fibo_infinitive()
# for el in f2:
#     print(el)


def programming_languages():
    try:
        yield 'Python'
        yield 'JavaScript'
        yield 'Java'
        yield 'Ruby'
        yield 'Scala'
        yield 'Rusty'
        yield 'Go'
        yield 'PHP'
        yield 'HTML'
        yield 'CSS'
        yield 'C++'
    except StopIteration:
        pass


p = programming_languages()
# next(p)
# print(p.send('Flutter'))
# for i in p:
#     print(i)
print(next(p))
print(next(p))
print(next(p))
# p.throw(StopIteration)
# p.throw(IndentationError)
# print(next(p))
# p.close()
# print(next(p))


def cube():
    while True:
        num: int = yield
        yield num**3


c = cube()
next(c)
print(c.send(10))
for i in range(1, 6):
    next(c)
    print(c.send(i))
    if i == 4:
        c.close()
