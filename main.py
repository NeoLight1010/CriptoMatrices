import numpy as np
from encode import encode_string


def main():
    string = "Las matrices son amigables"
    matrix = np.array([[1, 3], [1, 4]])

    print(encode_string(string, matrix, only_alpha=True))


if __name__ == "__main__":
    main()
