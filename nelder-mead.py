import numpy as np

def nelder_mead(f, initial_simplex, tol=1e-6, max_iter=1000, alpha=1.0, gamma=2.0, rho=0.5, sigma=0.5):

    """
    Parameters:
    f                   : objective function
    initial_simplex     : list of three points for 
    tol                 : limit for convergence
    max_iter            : maximum number of iterations to stop at
    alpha, gamma, rho, sigma: Parameters for reflection, expansion, contraction, and shrink

    Returns:
    Best point found and the function value at that point
    """

    # the simplex
    simplex = np.array(initial_simplex)
    num_iterations = 0

    while num_iterations < max_iter:

        simplex = sorted(simplex, key=lambda x: f(x))
        
        # identify the best, worst and second worst point from the simplex
        best = simplex[0]
        worst = simplex[-1]
        second_worst = simplex[-2]

        # calculate the centroid of the points excluding the worst
        centroid = np.mean(simplex[:-1], axis=0)

        # for reflection

        reflected = centroid + alpha * (centroid - worst)
        f_reflected = f(reflected)

        if f_reflected < f(best):
            
            # expansion
            expanded = centroid + gamma * (reflected - centroid)
            if f(expanded) < f_reflected:
                simplex[-1] = expanded
            else:
                simplex[-1] = reflected
        else:
            if f_reflected < f(second_worst):
                simplex[-1] = reflected
            else:
                # contraction
                if f_reflected < f(worst):
                    contracted = centroid + rho * (reflected - centroid)
                else:
                    contracted = centroid + rho * (worst - centroid)

                if f(contracted) < f(worst):
                    simplex[-1] = contracted
                else:
                    # shrink
                    for i in range(1, len(simplex)):
                        simplex[i] = best + sigma * (simplex[i] - best)

        # convergence
        if np.max(np.abs(simplex[0] - simplex[1:])) < tol:
            break

        num_iterations += 1

    # return the best point
    simplex = sorted(simplex, key=lambda x: f(x))
    return simplex[0], f(simplex[0])
