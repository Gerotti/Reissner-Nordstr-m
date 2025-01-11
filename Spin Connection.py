"Spin Connection"

def spin_connection_matrix(spin_connection, n):

    matrices = {}
    for mu in range(n):  # Iterate over μ
        # Create an empty matrix for the current μ
        matrix = sp.Matrix.zeros(n, n)
        for a in range(n):
            for b in range(n):
                if (a, b, mu) in spin_connection:
                    matrix[a, b] = spin_connection[(a, b, mu)]
                    # Apply anti-symmetry: w^{ab}_mu = -w^{ba}_mu
                    if a != b:
                        matrix[b, a] = -spin_connection[(a, b, mu)]
        matrices[mu] = matrix
    return matrices

from IPython.display import display, Math

def display_spin_connection(formatted_spin_connection):

    for mu, matrix in formatted_spin_connection.items():
        # Create a LaTeX representation for the matrix
        matrix_latex = sp.latex(matrix)
        display(Math(f"w_{{\mu = {mu}}} = {matrix_latex}"))


display_spin_connection(formatted_spin_connection)

