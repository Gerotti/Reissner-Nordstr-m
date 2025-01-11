"Gamma matrices"

import numpy as np

def define_gamma_matrices():
    """Define the 4x4 gamma matrices in the Dirac representation."""
    gamma_0 = np.array([[1, 0, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, -1, 0],
                        [0, 0, 0, -1]])

    gamma_1 = np.array([[0, 0, 0, 1],
                        [0, 0, 1, 0],
                        [0, -1, 0, 0],
                        [-1, 0, 0, 0]])

    gamma_2 = np.array([[0, 0, 0, -1j],
                        [0, 0, 1j, 0],
                        [0, 1j, 0, 0],
                        [-1j, 0, 0, 0]])

    gamma_3 = np.array([[0, 0, 1, 0],
                        [0, 0, 0, -1],
                        [-1, 0, 0, 0],
                        [0, 1, 0, 0]])

    return gamma_0, gamma_1, gamma_2, gamma_3

def multiply_gamma_matrices(gamma_matrices, index1, index2):
    """Multiply two gamma matrices based on their indices."""
    return np.dot(gamma_matrices[index1], gamma_matrices[index2])

def main():
    gamma_matrices = define_gamma_matrices()
    index1 = int(input("Enter the first index (0 to 3) for gamma matrix: "))
    index2 = int(input("Enter the second index (0 to 3) for gamma matrix: "))

    result = multiply_gamma_matrices(gamma_matrices, index1, index2)
    print("The product of gamma[{}] and gamma[{}] is:".format(index1, index2))
    print(result)


if __name__ == "__main__":
    main()
