class Scrabble:
    scores = {
        'aeioulnrst': 1,
        'dg':2,
        'bcmp': 3,
        'fhvwy':4,
        'k':5,
        'jx':8,
        'qz':10
    }

    @classmethod
    def get_letter_score(cls, letter):
        if not isinstance(letter, str):
            return 0
        else:
            for key in cls.scores:
                if letter.lower() in key:
                    return cls.scores[key]
            return 0
        
    def __init__(self, text = None):
        self.text = text

    @classmethod
    def calculate_score(cls, word = None):
        word = '' if word is None else word
        return sum(cls.get_letter_score(letter) for letter in word)
    
    def score(self):
        return self.__class__.calculate_score(self.text)
