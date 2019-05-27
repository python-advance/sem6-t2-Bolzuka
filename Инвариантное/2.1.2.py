
z = int(input('Введите количество чисел: '))

print('Ответ: ')

def fib(n):
  if n > 1:
    return fib(n-1) + fib(n-2)
  return n
for i in range(z):
  print(fib(i), end=' ')