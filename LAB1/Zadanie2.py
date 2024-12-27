from collections import deque

def bfs_najkrotsza_sciezka(graf, start, koniec):

    def bfs():

        kolejka = deque([(start, [start])])


        while kolejka:
            (wierzcholek, sciezka) = kolejka.popleft()


            for sasiad in graf.get(wierzcholek, []):
                if sasiad == koniec:
                    return sciezka + [sasiad]
                if sasiad not in sciezka:
                    kolejka.append((sasiad, sciezka + [sasiad]))


        return []


    return bfs()


przyklad_graf = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


startowy = 'A'
koncowy = 'F'


sciezka = bfs_najkrotsza_sciezka(przyklad_graf, startowy, koncowy)
print(f"Najkrótsza ścieżka z {startowy} do {koncowy}: {sciezka}")
