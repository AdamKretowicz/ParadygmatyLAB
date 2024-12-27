import numpy as np
from functools import reduce

def main():
    print("\n--- Program Łączenia Macierzy ---\n")


    print("Podaj listę macierzy (oddziel wiersze spacjami, a macierze przecinkami):")
    print("Przykład: '1 2; 3 4, 5 6; 7 8' oznacza dwie macierze: [[1, 2], [3, 4]] i [[5, 6], [7, 8]]")

    user_input = input("Wprowadź macierze: ")
    matrices = [np.array([list(map(int, row.split())) for row in matrix.split(';')]) for matrix in user_input.split(',')]

    print("\nDostępne operacje:")
    print("1. Dodawanie (np. 'a + b')")
    print("2. Mnożenie (np. 'a @ b')")
    print("3. Niestandardowa operacja")

    choice = input("Wybierz operację (1/2/3): ")

    if choice == '1':
        operation = "a + b"
    elif choice == '2':
        operation = "a @ b"
    elif choice == '3':
        print("\nPodaj operację w formacie Python (np. 'a - b', 'a * b', 'np.maximum(a, b)'):")
        operation = input("Operacja: ")
    else:
        print("Nieprawidłowy wybór!")
        return


    def matrix_operation(a, b):
        return eval(operation, {"a": a, "b": b, "np": np})


    try:
        result = reduce(matrix_operation, matrices)
        print("\nWynikowa macierz:")
        print(result)
    except Exception as e:
        print(f"\nWystąpił błąd podczas wykonywania operacji: {e}")

if __name__ == "__main__":
    main()