from constants import *
import numpy as np


def decode_string(
    encoded: str, key_matrix: np.ndarray, alpha_only: bool = False
) -> str:
    """Decodes an encoded string of format "[X1] [X2] [X3] [...] [Xn]".

    Assumes the given string has the correct n (n % key_matrix_n == 0)
    """
    matrix_n = key_matrix.shape[0]
    encoded_values = [int(x) for x in encoded.strip().split(" ")]

    # Group numbers
    value_groups = []
    for i in range(0, len(encoded_values), matrix_n):
        value_groups.append(np.array(encoded_values[i : i + matrix_n]))

    # Get decoded matrix
    matrix_inv = np.linalg.inv(key_matrix)
    decoded_matrices = []
    for group in value_groups:
        t = group.T
        decoded_group = np.dot(matrix_inv, t).T
        decoded_matrices.append(decoded_group)

    # Generate decoded string
    gap = ALPHA_GAP if alpha_only else 0
    decoded_str = ""
    for group in decoded_matrices:
        for element in group:
            decoded_str = decoded_str + chr(int(np.around(element + gap)))

    return decoded_str
