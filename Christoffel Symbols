"Christoffel Symbols"

import sympy as sp

#Symbols
t, r, theta, phi = sp.symbols('t r theta phi')
f = sp.Function('f')(r)
coords = [t, r, theta, phi]

#Reissner-Nordström metric tensor
#ds^2 = -f(r) dt^2 + (1/f(r)) dr^2 + r^2 dθ^2 + r^2 sin^2(θ) dφ^2
metric = sp.Matrix([
    [-f, 0, 0, 0],
    [0, 1/f, 0, 0],
    [0, 0, r**2, 0],
    [0, 0, 0, r**2 * sp.sin(theta)**2]
])


#Christoffel symbols
def christoffel_symbols(metric, coords):
    n = len(coords)
    christoffel = sp.MutableDenseNDimArray.zeros(n, n, n)
    inv_metric = metric.inv()  # Inverse of the metric

    for alpha in range(n):
        for mu in range(n):
            for nu in range(n):
                # Compute the Christoffel symbol Γ^alpha_mu_nu
                sum_term = 0
                for beta in range(n):
                    sum_term += inv_ metric[alpha, beta] * (
                        sp.diff(metric[beta, nu], coords[mu]) +
                        sp.diff(metric[beta, mu], coords[nu]) -
                        sp.diff(metric[mu, nu], coords[beta])
                    )
                christoffel[alpha, mu, nu] = sp.simplify(sum_term / 2)
    return christoffel

christoffel = christoffel_symbols(metric, coords)

#Results
christoffel
