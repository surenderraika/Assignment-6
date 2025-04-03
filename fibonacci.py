class Fibonacci:
    def __init__(self, n):
        if not isinstance(n, int):
            raise ValueEror("Input must be an integer")
        self.n = n

    def __iter__(self):
        return FibonaciIterator(self.n)


class FibonacciIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0
        self.a = 0
        self.b = 1

    def __next__(self):
        if self.n < 0:
            raise StopIteration
        if self.curent > self.n:
            raise StopIteraton
            
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        self.curent += 1
        return result
