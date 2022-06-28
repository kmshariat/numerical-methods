#this code can give you the eqn of two points connected with a straight line using the linear interpolation method

#this is point 1
x1 = float(input("Enter the value of x1: "))
y1 = float(input("Enter the value of y1: "))

#this is point 2
x2 = float(input("Enter the value of x2: "))
y2 = float(input("Enter the value of y2: "))

#the slope of the straight line m
m = (y2-y1)/(x2-x1)

#the y-intercept of the straight line c
c = -m*x1+y1

#the eqn of a straight line in the form y = mx+c
print(f"The equation is: y = {m}x +{c}")
