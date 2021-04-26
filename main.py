from decode import decode_string
import numpy as np
from encode import encode_string


def main():
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


if __name__ == "__main__":
    main()
