from functools import reduce

def optymalizacja_proceduralna(zadania):


    zadania.sort(key=lambda x: x[0])


    czas_oczekiwania = 0
    suma_czasow = 0
    for czas, _ in zadania:
        czas_oczekiwania += suma_czasow
        suma_czasow += czas

    return zadania, czas_oczekiwania

def optymalizacja_funkcyjna(zadania):

    zadania_posortowane = sorted(zadania, key=lambda x: x[0])


    czas_oczekiwania = reduce(lambda acc, czas: (acc[0] + acc[1], acc[1] + czas[0]), zadania_posortowane, (0, 0))[0]

    return zadania_posortowane, czas_oczekiwania


zadania = [(3, 50), (1, 20), (2, 30), (5, 10)]


kolejnosc_proceduralna, czas_proceduralny = optymalizacja_proceduralna(zadania)
print("[Proceduralne]")
print(f"Optymalna kolejność zadań: {kolejnosc_proceduralna}")
print(f"Całkowity czas oczekiwania: {czas_proceduralny}")


kolejnosc_funkcyjna, czas_funkcyjny = optymalizacja_funkcyjna(zadania)
print("\n[Funkcyjne]")
print(f"Optymalna kolejność zadań: {kolejnosc_funkcyjna}")
print(f"Całkowity czas oczekiwania: {czas_funkcyjny}")