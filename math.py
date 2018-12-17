# Example function
print("---")

def fib(x):
  if x <= 1:
    return 1
  return x * fib(x-1)

y = int(input("Input number: "))
f = fib(y)
print (str(y) + "!", "=", f)