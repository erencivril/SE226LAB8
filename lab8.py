from abc import ABC, abstractmethod


class TxtReceiver(ABC):
    def __init__(self, address):
        self.address = address

    def calculateFreqs(self):
        pass

class ListCount(TxtReceiver):
    def calculateFreqs(self):
        frequencies = [0] * 26
        with open(self.address, 'r') as file:
            for line in file:
                for letter in line:
                    letter = letter.lower()
                    if letter.isalpha():
                        index = ord(letter) - ord('a')
                        frequencies[index] += 1
        for i, freq in enumerate(frequencies):
            if freq > 0:
                letter = chr(ord('a') + i)
                print("List Count ---> " + letter + " Resulting List -> " + letter + " = " + str(freq))

class DictCount(TxtReceiver):
    def calculateFreqs(self):
        frequencies = {}
        with open(self.address, 'r') as file:
            for line in file:
                for letter in line:
                    letter = letter.lower()
                    if letter.isalpha():
                        if letter in frequencies:
                            frequencies[letter] += 1
                        else:
                            frequencies[letter] = 1
        sorted_frequencies = dict(sorted(frequencies.items()))
        for letter, freq in sorted_frequencies.items():
            print("Dict Count ---> " + letter + " Resulting List -> " + letter + " = " + str(freq))






weirdWORDS = "weirdWords.txt"

listCounter = ListCount(weirdWORDS)
listCounter.calculateFreqs()
print("------------------------------------------------------")
dictCounter = DictCount(weirdWORDS)
dictCounter.calculateFreqs()
