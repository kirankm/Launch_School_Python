'''
PEDAC
Problem

Input: number
Output:
    class called RomanNumeral
        -> Won't take negative numbers
        Has an instance variable storing the number
    
        has a method called to_roman to convert it to a roman numeral

        has a class Variable storing the different conversions
        
        to_roman
            Input: Number
            Output: String representing roman form
            Algorithm:
                1) Get each digit multiplied by it's place
                2) So 163 becomes : 1*100, 6*10, and 3
                3) Use get roman_version to get the roman version of that number
                4) Concatenate each individual string
        get_roman_numeral
        Algorithm:
            1) Get closest numeral
                if starts with 4 or 9, get closest negative
                if starts with anything else, get closest positive
'''

class RomanNumeral:
    roman_letters = {
        1: 'I',
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M"
    }

    subtractive_roman_numerals = {
        1: 'I',
        10: "X",
        100: "C"
    }

    def __init__(self, num):
        self.num = num

    @classmethod
    def get_roman_numeral(cls, num):
        pass

    @classmethod
    def closest_larger(cls, val):
        index = len([num for num in cls.roman_letters.keys() if num < val])
        return list(cls.roman_letters.keys())[index]

    @classmethod
    def closest_smaller(cls, search_dict, val):
        index = len([num for num in search_dict.keys() if num < val]) - 1
        return list(search_dict.keys())[index]
    
    @classmethod
    def get_roman_numeral(cls, num):
        if num in cls.roman_letters:
            return cls.roman_letters[num]
        if str(num).startswith('4') or str(num).startswith('9'):
            return cls.get_roman_numeral_subtractive(num)
        return cls.get_roman_numeral_additive(num)
    
    @classmethod
    def get_roman_numeral_subtractive(cls, num):
        base_num = cls.closest_larger(num)
        sub_num = cls.closest_smaller(cls.subtractive_roman_numerals, base_num)
        return cls.roman_letters[sub_num] + cls.roman_letters[base_num]

    @classmethod
    def get_roman_numeral_additive(cls, num):
        curr_num = num
        result = ''
        while curr_num not in cls.roman_letters:
            base_num = cls.closest_smaller(cls.roman_letters, curr_num)
            result += cls.roman_letters[base_num]
            curr_num -= base_num
        return result + cls.roman_letters[curr_num]
    
    def to_roman(self):
        dividing_value = 1
        curr_num = self.num
        result = ''
        while True:
            divisor, remainder = divmod(curr_num, dividing_value)
            dividing_value = dividing_value * 10
            curr_num = curr_num - remainder
            if remainder != 0:
                result = RomanNumeral.get_roman_numeral(remainder) + result
            if divisor == 0:
                return result
