#Golden Ratio using formula phi = sum(1/n**2) from 1 to infinity
#slow converge to phi the golden ratio

def phi(iteration):
    phi = 0
    for i in range(iteration):
        phi = phi + 1/(i+1)**2
        print(f"After {i+1} iteration: phi = {phi}")
    return phi
