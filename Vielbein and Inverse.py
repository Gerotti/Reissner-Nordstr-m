"Vielbein and Inverse"

#Minkowski (-1, +1, +1, +1)
eta = sp.diag(-1, 1, 1, 1)

#Vielbein components
#e^a_mu * e^b_nu * η_ab = g_mu_nu
vielbein = sp.Matrix([
    [sp.sqrt(f), 0, 0, 0],
    [0, sp.sqrt(1/f), 0, 0],
    [0, 0, r, 0],
    [0, 0, 0, r * sp.sin(theta)]
])

#Inverse vielbein
inverse_vielbein = sp.Matrix([
    [-1/sp.sqrt(f), 0, 0, 0],
    [0, sp.sqrt(f), 0, 0],
    [0, 0, 1/r, 0],
    [0, 0, 0, 1/(r * sp.sin(theta))]
])

display(vielbein)
display(inverse_vielbein)
