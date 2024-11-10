# square root algorithm 
# computes the square root of any number using iterative methods

def root(num):
    root = 1
    for _ in range(100):
        root = 0.5 * (root + num / root)

    return root 
