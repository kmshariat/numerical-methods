#Newton Raphson Method
def f(x):
  return x**3 - 3*x**2 +5*x - 7
def df(x):
  return 3*x**2 - 6*x + 5 
x = 2
for i in range(10):
  x = x - f(x)/df(x)
  print(x)
