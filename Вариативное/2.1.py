# 2.1. Разработать функцию, возвращающую список чисел ряда Фибоначчи с использованием бесконечных итераторов (модуль itertools).

from itertools import islice

class FibonacciGenerator:
    """
      Итерируемый объектом тк реализует метод __iter__ и итератором тк реализует метод __next__
    """
    def __init__(self):
        self.fib1 = 0
        self.fib2 = 1
    def __next__(self):
        result = self.fib1
        self.fib1, self.fib2 = self.fib2, self.fib1 + self.fib2
        return result
    def __iter__(self):
        return self

fib = FibonacciGenerator()  # создаем объект, в котором описываем правила для задачи

start = int(input("Число От: "))
stop = int(input("Число До: "))
"""
itertools.islice(iterable[, start], stop[, step]) - итератор, состоящий из среза.
"""
print(list(islice(fib, start, stop)))
