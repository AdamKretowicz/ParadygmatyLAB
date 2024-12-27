def podzial_paczek(wagi, max_waga):

    wagi.sort(reverse=True)

    kursy = []

    for waga in wagi:

        przypisano = False


        for kurs in kursy:
            if sum(kurs) + waga <= max_waga:
                kurs.append(waga)
                przypisano = True
                break


        if not przypisano:
            kursy.append([waga])


    return len(kursy), kursy


wagi_paczek = [5, 10, 7, 3, 8, 2, 6, 11, 14, 1]
max_waga_kursu = 15
liczba_kursow, podzial = podzial_paczek(wagi_paczek, max_waga_kursu)

print(f"Minimalna liczba kursów: {liczba_kursow}")
print("Podział paczek na kursy:")
for i, kurs in enumerate(podzial, 1):
    print(f"Kurs {i}: {kurs}")


