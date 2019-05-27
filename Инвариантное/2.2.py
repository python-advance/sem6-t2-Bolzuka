
n = int(input('Введите количество чисел: '))

class FibonacciGenerator:
    def __init__(self):
        self.fib1 = 0
        self.fib2 = 1
    def __next__(self):
        result = self.fib1
        self.fib1, self.fib2 = self.fib2, self.fib1 + self.fib2
        return result
    def __iter__(self):
        return self

print('Ответ: ')
for i in FibonacciGenerator():
    print(i, end=' ')

    if i > 90:
        break