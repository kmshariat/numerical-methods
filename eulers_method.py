#Euler's Method

import numpy as np

#defining the derivative
def f(x,y):
  return (y*np.log(y))/x

h = float(input("Enter step size: ")) #step size
x = float(input("Enter initial guess for x: ")) #initial guess about the x-coordinate
y = float(input("Enter initial guess for y: ")) #initial guess about the y-coordinate 
iteration = int(input("Enter how many iterations: ")) #iteartion number

for i in range(iteration):
  y = y + f(x,y)*h 
  x = x + h
  print(f"After {i} iteration for x: {x} corresponding y: {y}")
