class Banner:
    def __init__(self, msg, width = None):
        self._message = msg
        self.width = width

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, banner_width):
        self._width = self.process_banner_width(banner_width)
    
    def process_banner_width(self, banner_width):
        if banner_width is None:
            return len(self.message) + 2
        elif not isinstance(banner_width,int):
            raise Exception(ValueError, 'Only Integers are Allowed for Banner Width')
        else:
            return max(len(self.message) + 2, banner_width)

    @property
    def message(self):
        return self._message
    
    def __str__(self):
        return "\n".join([self._horizontal_rule(),
                          self._empty_line(),
                          self._message_line(),
                          self._empty_line(),
                          self._horizontal_rule()])

    def _empty_line(self):
        return self.get_full_line('|', ' ')

    def _horizontal_rule(self):
        return self.get_full_line('+', '-')

    def _message_line(self):
        return f"|{self.message.center(self.width)}|"

    def get_center_part(self, char):
        return char * (self.width)
    
    def get_full_line(self, border_char, fill_char):
        return f"{border_char}{self.get_center_part(fill_char)}{border_char}"
    # Comments show expected output

banner = Banner('To boldly go where no one has gone before.', 12)
print(banner)
# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+

banner = Banner('', 10)
print(banner)
# +--+
# |  |
# |  |
# |  |
# +--+