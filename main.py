from decode import decode_string
import numpy as np
from encode import encode_string
import sys


def main():
    argv = sys.argv

    mode = argv[1]

    if mode == "test":
        test()
        return

    string = argv[2]
    matrix_n = len(argv) - 1 - 2

    # Generate key matrix
    key_matrix = []
    for i in range(matrix_n):
        row_str = argv[3 + i]
        key_matrix.append(np.fromstring(row_str, dtype=int, sep=" "))
    key_matrix = np.array(key_matrix)

    if mode == "encode":
        encoded = encode_string(string, key_matrix, True)
        print(encoded)

    if mode == "decode":
        decoded = decode_string(string, key_matrix, True)
        print(decoded)


def test():
    string = "Las matrices son amigables"
    matrix = np.array([[1, 3], [1, 4]])
    encoded = "15 16 58 71 61 81 45 54 18 23 76 95 57 71 40 53 30 37 7 9 27 32 91 115"

    print(
        f'Encode "Las matrices son amigables": {encode_string(string, matrix, only_alpha=True)}'
    )
    print()
    print(
        f"Decoding previous output: {decode_string(encoded, matrix, alpha_only=True)}"
    )

    print()
    matrix = np.array([[1, -1, 0], [4, -2, 3], [2, 1, 5]])
    encoded = "8 63 66 2 106 161 -2 1 10 -6 19 53 -6 96 180"
    print(f"Decode {encoded}")
    print(f"Decoded: {decode_string(encoded, matrix, alpha_only=True)}")

    string = "tu mayor enemigo eres tu mismo"
    matrix = np.array([[-1, -2, 2], [-1, -1, 3], [-1, -1, -4]])
    print(f'\nEncode "{string}"')
    print(f"Encoded: {encode_string(string, matrix, only_alpha=True)}")

    print(
        decode_string(
            "78 220 71 61 123 49 86 171 74 41 37 29 93 128 81 41 216 54",
            np.array([[1, 3, 1], [5, 2, 6], [2, 2, 1]]),
            True,
        )
    )


if __name__ == "__main__":
    # test()
    main()
