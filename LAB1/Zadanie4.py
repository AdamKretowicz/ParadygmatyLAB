def algorytm_plecakowy_proceduralny(przedmioty, pojemnosc):

    n = len(przedmioty)
    dp = [[0] * (pojemnosc + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        waga, wartosc = przedmioty[i - 1]
        for j in range(1, pojemnosc + 1):
            if waga <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - waga] + wartosc)
            else:
                dp[i][j] = dp[i - 1][j]


    wybrane = []
    j = pojemnosc
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            wybrane.append(przedmioty[i - 1])
            j -= przedmioty[i - 1][0]

    return dp[n][pojemnosc], wybrane

def algorytm_plecakowy_funkcyjny(przedmioty, pojemnosc):

    def rozwiaz(dp, przedmioty, pojemnosc):
        if not przedmioty:
            return dp, []

        waga, wartosc = przedmioty[0]
        nowe_dp = {
            j: max(dp.get(j, 0), dp.get(j - waga, 0) + wartosc) if j >= waga else dp.get(j, 0)
            for j in range(pojemnosc + 1)
        }

        dp, wybrane = rozwiaz(nowe_dp, przedmioty[1:], pojemnosc)

        if nowe_dp[pojemnosc] != dp.get(pojemnosc, 0):
            wybrane.append((waga, wartosc))

        return nowe_dp, wybrane

    dp, wybrane = rozwiaz({}, przedmioty, pojemnosc)
    return dp.get(pojemnosc, 0), wybrane


przedmioty = [(2, 3), (3, 4), (4, 5), (5, 8)]
pojemnosc_plecaka = 5


maks_wartosc_proc, wybrane_proc = algorytm_plecakowy_proceduralny(przedmioty, pojemnosc_plecaka)
print("[Proceduralne]")
print(f"Maksymalna wartość: {maks_wartosc_proc}")
print(f"Wybrane przedmioty: {wybrane_proc}")


maks_wartosc_funk, wybrane_funk = algorytm_plecakowy_funkcyjny(przedmioty, pojemnosc_plecaka)
print("\n[Funkcyjne]")
print(f"Maksymalna wartość: {maks_wartosc_funk}")
print(f"Wybrane przedmioty: {wybrane_funk}")