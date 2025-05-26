class Student:
    school_name = "Oxford"

    @classmethod
    def get_school_name(cls):
        return cls.school_name

    def __init__(self, name):
        self.name = name


print(Student.get_school_name())
print(Student.school_name)