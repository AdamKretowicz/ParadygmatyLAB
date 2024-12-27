def harmonogramowanie_proceduralne(zadania):

    zadania.sort(key=lambda x: x[1])


    wybrane = []
    ostatni_czas_zakonczenia = 0
    maks_nagroda = 0

    for start, koniec, nagroda in zadania:
        if start >= ostatni_czas_zakonczenia:
            wybrane.append((start, koniec, nagroda))
            ostatni_czas_zakonczenia = koniec
            maks_nagroda += nagroda

    return maks_nagroda, wybrane

def harmonogramowanie_funkcyjne(zadania):

    zadania_posortowane = sorted(zadania, key=lambda x: x[1])


    def wybierz_zadania(zadania, ostatni_czas_zakonczenia=0):
        if not zadania:
            return 0, []

        start, koniec, nagroda = zadania[0]
        if start >= ostatni_czas_zakonczenia:
            nagroda_ze_zadaniem, wybrane_ze_zadaniem = wybierz_zadania(zadania[1:], koniec)
            nagroda_ze_zadaniem += nagroda

            nagroda_bez_zadania, wybrane_bez_zadania = wybierz_zadania(zadania[1:], ostatni_czas_zakonczenia)

            if nagroda_ze_zadaniem > nagroda_bez_zadania:
                return nagroda_ze_zadaniem, [(start, koniec, nagroda)] + wybrane_ze_zadaniem
            else:
                return nagroda_bez_zadania, wybrane_bez_zadania

        else:
            return wybierz_zadania(zadania[1:], ostatni_czas_zakonczenia)

    maks_nagroda, wybrane = wybierz_zadania(zadania_posortowane)
    return maks_nagroda, wybrane


zadania = [(1, 3, 50), (2, 5, 20), (4, 6, 30), (6, 7, 25), (5, 8, 15)]


maks_nagroda_proc, wybrane_proc = harmonogramowanie_proceduralne(zadania)
print("[Proceduralne]")
print(f"Maksymalna nagroda: {maks_nagroda_proc}")
print(f"Wybrane zadania: {wybrane_proc}")


maks_nagroda_funk, wybrane_funk = harmonogramowanie_funkcyjne(zadania)
print("\n[Funkcyjne]")
print(f"Maksymalna nagroda: {maks_nagroda_funk}")
print(f"Wybrane zadania: {wybrane_funk}")