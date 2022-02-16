#Bi section method more on this can be found here : https://en.wikipedia.org/wiki/Bisection_method 

#here goes the function
def f(x):
  return x**3-x-2

#user gives the value of the domain where the root can be found
a = float(input("Enter lower limit: "))
b = float(input("Enter upper limit: "))
iteration = int(input("Enter how many times you want to iterate: "))

print("Iteration --> a --> b -->c --> f(c)")
print("-"*50)

if a<b:
  for i in range(iteration):
    c = (a+b)/2
    if f(c) <0:
      a = c
    elif f(c) >0:
      b = c
    elif f(c) == 0:
      print(c)
      break
    print(f"{iteration}-->{a}-->{b}-->{c}-->{f(c)}")
else:
  print("You put the limit in reverse")
