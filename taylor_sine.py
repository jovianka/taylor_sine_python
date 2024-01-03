from matplotlib import pyplot as plt
import numpy as np
import math

# 4b
def taylor_sine_plot(k, Nx, xmin, xmax, a = 0, N = 2):
    def f(x):
        return np.sin(k * x)
    

    def y(x):
        res = 0.0
        sign = 1
        for n in range(1, N + 1, 2):
            yn = (sign * k**n / math.factorial(n)) * (x - a)**n
            res += yn
            sign = -sign

        return res


    plt.figure(figsize=(10, 10))
    ax1 = plt.subplot(111)
    ax1.axis([xmin, xmax, -2, 2])
    
    ax1.set_title('sin(x) approximation using Taylor Series', fontsize=16)
    ax1.set_xlabel('$x$', fontsize=16)
    
    # y = 0
    ax1.axhline(y=0, color='r', linestyle='-')
    
    # define our x for plotting purposes
    x = np.linspace(xmin, xmax, 1000, dtype=float)
    
    # plot exact function
    ax1.plot(x, f(x), 'b', lw=3, label='Exact function')
    
    # plot dot (red o) at x = a
    ax1.plot(a, y(a), 'ro')
    
    # plot the approximation
    ax1.plot(x, y(x), 'k', lw=2, label='Taylor approximation')

    # highlight xi
    for i in range(0, Nx + 1):
        xi = xmin + i * (xmax - xmin) / Nx
        ax1.plot(xi, y(xi), 'ro')
        ax1.annotate(f"x = {xi}\ny = {y(xi)}", xy=(xi, y(xi)), xytext=(20, 5), textcoords='offset pixels')

    
    ax1.legend(loc='best', fontsize=14)
    plt.show()


# 4c
def taylor_sine_absolute_error(y, k, a, N):
    def f(x):
        return np.sin(k * x)

    def t(x):
        res = 0.0
        sign = 1
        for n in range(1, N + 1, 2):
            yn = (sign * k**n / math.factorial(n)) * (x - a)**n
            res += yn
            sign = -sign

        return res

    return abs(f(y) - t(y))


# 4d
def taylor_sine_mae(k, Nx, xmin, xmax, a = 0, N = 2):
    sum = 0
    for i in range(0, Nx + 1):
        xi = xmin + i * (xmax - xmin) / Nx
        sum += taylor_sine_absolute_error(xi, k, a, N)

    sum = sum / (Nx + 1)

    return sum
    


k = 1
Nx = 6
xmin = -2 * np.pi
xmax = 2 * np.pi
a = 0
N = 4
y = 0

taylor_sine_plot(k, Nx, xmin, xmax, a, N)
print(taylor_sine_absolute_error(y, k, a, N))
print(taylor_sine_mae(k, Nx, xmin, xmax, a, N))