class DynamicExtreme:
    def __init__(self, data):
        self.data = data

    def gethighestnum(self):
        highest = float('-inf')
        for i in range(len(self.data)):
            number = self.parsetoint(self.data[i])

            if type(number) == int and number > highest:
                highest = number
        return "not found" if highest == float('-inf') else highest

    def parsetoint(self, number):
        try:
            return int(number)
        except:
            return None
    def findlongeststring(self):
        longest = 0
        longeststring = ""
        for string in self.data:
            if type(string) == str and len(string) > longest:
                longest = len(string)
                longeststring = string
        return longeststring

    def findlongesttuple(self):
        longest = 0
        longesttuple = ""
        tupel = list(filter(lambda item: type(item) == tuple, self.data))
        for tup in tupel:
            if len(tup) > longest:
                longest = len(tup)
                longesttuple = tup
        return longesttuple

listData = [(1, 6), "Ania", "bartek", "siema", "-23", 22, (1, 2, 3), (4, 5, 6, 5)]
obiekt = DynamicExtreme(listData)
print(obiekt.gethighestnum())
print(obiekt.findlongeststring())
print(obiekt.findlongesttuple())

