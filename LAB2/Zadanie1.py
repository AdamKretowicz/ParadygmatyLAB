from operator import itemgetter


def analizaTekstu(tekst):
    words = tekst.split()
    countOfWords = len(tekst.split())
    countOfSentences = sum(1 for znak in tekst if znak in '.!?')
    countOfNewline = tekst.strip().count('\n\n') + 1 if tekst.strip() else 0
    print("Liczbna słów:",countOfWords)
    print("Liczba zdań:",countOfSentences)
    print("Liczba akapitów:",countOfNewline)

    freqWords = dict()
    for word in words:
         if word not in ["i", "and", "the", "an", "a"]:
            if word not in freqWords:
                freqWords[word] = 1
            else:
                freqWords[word] += 1
    # filtered = dict(filter(lambda item: item[::2], freqWords.items()))
    # print(filtered)
    sortedFreqWords = sorted(freqWords.items(), key=itemgetter(1), reverse = True)
    firstThree = sortedFreqWords[:3]
    print(firstThree)

    for slowo in words:
        if slowo[0].lower() == 'a':
            print(slowo,"->", slowo[::-1].replace('.', ''))

analizaTekstu("Ależ ten las jest niezwykły! Czy Andrzej zauważył te ogromne, stare drzewa? Ania zawsze zachwyca się ich wysokością i korą pełną wzorów. Jak dobrze spacerować tutaj razem w ciszy! Czy to nie najlepszy sposób na odpoczynek?")