def fact(n):  
    return 1 if (n==1 or n==0) else n * fact(n - 1);  

#formula for euler number e = sum(1/n!) from 0 to infinity

def eulerconst(iteration):
    e = 0
    for i in range(iteration):
        e = e + 1/fact(i)
        print(f"After {i+1} iteration: e = {e}")
    return e
