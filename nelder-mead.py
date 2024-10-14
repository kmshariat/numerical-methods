import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

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
    simplices = [simplex.copy()]  # to store the history of the simplex

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

        simplices.append(np.array(simplex))

        # convergence
        if np.max(np.abs(simplex[0] - simplex[1:])) < tol:
            break

        num_iterations += 1

    simplex = sorted(simplex, key=lambda x: f(x))
    return simplex[0], f(simplex[0]), simplices





# -------------------------------------------------
#                   TESTING
# -------------------------------------------------

def three_hump_camel(x):
    return 2 * x[0]**2 - 1.05 * x[0]**4 + (x[0]**6) / 6 + x[0] * x[1] + x[1]**2

initial_simplex = [[-1,-2], [-3, -2], [-1.5, -1.5]]  # initial guess for the simplex
result, function_value, simplices = nelder_mead(three_hump_camel, initial_simplex)

# visualization using animation

fig, ax = plt.subplots()
x = np.linspace(-3, 3, 400)
y = np.linspace(-3, 3, 400)
X, Y = np.meshgrid(x, y)
Z = 2 * X**2 - 1.05 * X**4 + (X**6) / 6 + X * Y + Y**2

ax.contour(X, Y, Z, levels=np.linspace(np.min(Z), np.max(Z), 35))

simplex_plot, = plt.plot([], [], 'ro-', lw=2)
point_plot, = plt.plot([], [], 'bo')  # Current best point

def init():

    # initialize the animation
    simplex_plot.set_data([], [])
    point_plot.set_data([], [])
    return simplex_plot, point_plot

def update(frame):
    simplex = simplices[frame]
    simplex_plot.set_data(simplex[:, 0], simplex[:, 1])
    point_plot.set_data(simplex[0, 0], simplex[0, 1])
    ax.set_title(f"Iteration: {frame}")
    return simplex_plot, point_plot

anim = FuncAnimation(fig, update, frames=len(simplices), init_func=init, blit=True, repeat=False)

plt.xlabel("$x$")
plt.ylabel("$y$")
plt.title("Nelder-Mead Optimization")
plt.show()
