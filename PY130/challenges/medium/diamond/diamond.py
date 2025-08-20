class Diamond:
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    @classmethod
    def make_diamond(cls, letter):
        diamond_width = cls.get_diamond_width(letter)
        diamond = [''] * diamond_width
        for i in range(1 + diamond_width // 2):
            row = cls.construct_letter_row(cls.letters[i])
            diamond[i] = row
            diamond[diamond_width - i -1] = row
        diamond = [row.center(diamond_width) for row in diamond]
        return "\n".join(diamond) + "\n"
        

    @classmethod
    def get_diamond_width(cls, letter):
        return 2 * cls.letters.index(letter) + 1

    @classmethod
    def construct_letter_row(cls, letter):
        row_width = cls.get_diamond_width(letter)
        row_list = [' ']*row_width
        row_list[0] = letter
        row_list[row_width - 1] = letter
        return "".join(row_list)
        
        
