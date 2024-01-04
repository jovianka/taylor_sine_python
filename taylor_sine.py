from matplotlib import pyplot as plt
import numpy as np
import math

# 4b
def taylor_sine_plot(k, Nx, xmin, xmax, a, N):
    def f(x):
        return np.sin(k * x)


    def y(x):
        res = 0.0

        ## this can also be used if you only want to approximate at a = 0
        # sign = 1
        # for n in range(1, N + 1, 2):
        #     yn = (sign * k**n / math.factorial(n)) * (x - a)**n
        #     res += yn
        #     sign = -sign

        for n in range(0, N + 1, 1):
            dydx = np.sin(k*a + (0.5 * np.pi * n) * k**n)
            res += (dydx / math.factorial(n)) * (x - a) ** n

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
    sum = 0.0
    for i in range(0, Nx + 1):
        xi = xmin + i * (xmax - xmin) / Nx
        sum += taylor_sine_absolute_error(xi, k, a, N)

    sum = sum / (Nx + 1)

    return sum
    

action = ""
print("Sine Approximation using Taylor Series\n[0] Approximation Plot [1] Find Absolute Error [2] Find Mean Absolute Error")
action = input("Which action do you want? ")

match action:
    case "0":
        k = float(input("k = "))
        Nx = int(input("Nx = "))
        xmin = float(input("xmin = "))
        xmax = float(input("xmax = "))
        a = float(input("a = "))
        N = int(input("N = "))
        taylor_sine_plot(k, Nx, xmin, xmax, a, N)    

    case "1":
        y = float(input("y = "))
        k = float(input("k = "))
        a = float(input("a = "))
        N = int(input("N = "))
        print(f"Absolute error at x = {y}: {taylor_sine_absolute_error(y, k, a, N)}")

    case "2":
        k = float(input("k = "))
        Nx = input("Nx = ")
        xmin = float(input("xmin = "))
        xmax = float(input("xmax = "))
        a = float(input("a = "))
        N = int(input("N = "))
        print(f"Mean absolute error at xmin = {xmin} and xmax = {xmax}\nMAE = {taylor_sine_mae(k, Nx, xmin, xmax, a, N)}")
    
    case _:
        print("invalid action")