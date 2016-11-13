class Fibonnaci:
    def __init__(self):
        self.a = 1
        self.b = 1
        self.i = -1

    def next(self):
        self.i += 1
        if self.i < 2:
            return 1
        else:
            c = self.a + self.b
            self.a = self.b
            self.b = c
            return c
def next_fib():
    fibs = Fibonnaci()
    while len(str(fibs.next())) < 1000:
        pass
    return fibs.i + 1

print next_fib()
