from scipy.integrate import dblquad

def integrand(y, x):
    return x**2 + y**2

x_lower, x_upper = 0, 3
y_lower = lambda x: 0
y_upper = lambda x: 1

volume, error = dblquad(integrand, x_lower, x_upper, y_lower, y_upper)
print(f"Volume under surface z = x^2 + y^2: {volume:.1f}")
