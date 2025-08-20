class Anagram:
    def __init__(self, text):
        self.text = text.lower()
        self._sorted_text = sorted(self.text)

    def match(self, array_of_strings):
        return [string for string in array_of_strings 
                        if (sorted(string.lower()) == self._sorted_text) 
                        and (string.lower() != self.text)]