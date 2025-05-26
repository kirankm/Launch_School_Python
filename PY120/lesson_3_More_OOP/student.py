

students = {'John': 25, 'Jane': 22, 'Doe': 30}

def get_age(student):
    try:
        return students[student]
    except KeyError:
        return "Student Not Found"
    

print(get_age("John"))

print(get_age("Jhon"))