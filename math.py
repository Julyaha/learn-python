# Example function
print("---")

def factorial(x):
  if x <= 1:
    return 1
  return x * factorial(x-1)

  
def sqrt(x, y = 0.5):
  return x ** y



y = int(input("Input number: "))
f = factorial(y)
print (str(y) + "!", "=", f)
print ("Square root:", sqrt(y))