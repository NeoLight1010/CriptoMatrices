import numpy as np
import re


FILL_CHARACTER = "."


def encode_string(string: str, matrix: np.ndarray, only_alpha=False) -> str:
    matrix_n = matrix.shape[0]

    if only_alpha:
        # Remove non alphabetic characters and spaces
        non_alpha = re.compile("[^a-zA-Z]")
        string = non_alpha.sub("", string)
        string = string.lower()

    # Fill last characters
    string = string + (FILL_CHARACTER * (len(string) % matrix_n))

    # Group characters
    str_groups = []
    for i in range(0, len(string), matrix_n):
        str_groups.append(string[i : i + matrix_n])

    # Generate numeric groups
    gap = 96 if only_alpha else 0
    num_groups = []
    for str_group in str_groups:
        group = []
        for char in str_group:
            group.append(ord(char) - gap)
        num_groups.append(group)

    # Encode groups
    encoded_groups = []
    for group in num_groups:
        group_arr = np.array(group).T
        encoded_arr = np.dot(matrix, group_arr)
        encoded_groups.append(encoded_arr)

    # Return encoded str
    encoded_str = ""
    for group in encoded_groups:
        t = group.T
        for element in t:
            encoded_str = encoded_str + f"{element} "

    return encoded_str


def main():
    string = "Las matrices son amigables"
    matrix = np.array([[1, 3], [1, 4]])

    print(encode_string(string, matrix, only_alpha=True))


if __name__ == "__main__":
    main()
