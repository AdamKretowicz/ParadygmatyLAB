import numpy as np


def validate_and_execute(operation, matrices):

    try:
        if operation.startswith("add"):

            matrices_involved = operation[4:-1].split(",")
            matrices_involved = [m.strip() for m in matrices_involved]

            if len(matrices_involved) != 2:
                return "Błąd: Operacja dodawania wymaga dokładnie dwóch macierzy."

            mat1, mat2 = matrices[matrices_involved[0]], matrices[matrices_involved[1]]
            if mat1.shape != mat2.shape:
                return "Błąd: Macierze muszą mieć te same wymiary do dodawania."

            result = mat1 + mat2

        elif operation.startswith("multiply"):

            matrices_involved = operation[9:-1].split(",")
            matrices_involved = [m.strip() for m in matrices_involved]

            if len(matrices_involved) != 2:
                return "Błąd: Operacja mnożenia wymaga dokładnie dwóch macierzy."

            mat1, mat2 = matrices[matrices_involved[0]], matrices[matrices_involved[1]]
            if mat1.shape[1] != mat2.shape[0]:
                return "Błąd: Macierze mają niezgodne wymiary do mnożenia."

            result = mat1 @ mat2

        elif operation.startswith("transpose"):

            matrix_name = operation[10:-1].strip()
            if matrix_name not in matrices:
                return f"Błąd: Macierz '{matrix_name}' nie istnieje."

            result = matrices[matrix_name].T

        else:
            return "Błąd: Nieobsługiwana operacja. Obsługiwane operacje to add, multiply, transpose."

        return result

    except Exception as e:
        return f"Błąd: {str(e)}"



if __name__ == "__main__":
    # Przykładowe macierze
    matrices = {
        "matrix1": np.array([[1, 2], [3, 4]]),
        "matrix2": np.array([[5, 6], [7, 8]]),
        "matrix3": np.array([[1, 2, 3], [4, 5, 6]])
    }


    operations = [
        "add(matrix1, matrix2)",
        "multiply(matrix1, matrix3)",
        "transpose(matrix1)",
        "add(matrix1, matrix3)",
        "multiply(matrix2, matrix1)"
    ]

    for op in operations:
        print(f"Operacja: {op}")
        result = validate_and_execute(op, matrices)
        print(f"Wynik:\n{result}\n")
