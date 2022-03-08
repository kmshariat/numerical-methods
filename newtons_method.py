#Newton Raphson Method

#this function takes the function
def f(x):
  return x**3 - 3*x**2 +5*x - 7

#this function takes the derivative
def df(x):
  return 3*x**2 - 6*x + 5 

#user input for initial guess
x = float(input("Enter your initial guess: "))

#if df(x)==0 then the denominator in N-R method becomes zero hence the solution becomes undefined
if df(x) == 0:
  print("Solution is not possible using N-R Method")
else:
  for i in range(10):
    x = x - f(x)/df(x)
    print(f"After {i}th iteration the root is: {x}")
