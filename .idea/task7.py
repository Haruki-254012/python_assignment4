class Person:
    def __init__(self, name):
        self.name = name

    def get_role(self):
        pass

class Teacher(Person):
    def get_role(self):
        return f"{self.name} is a Teacher"

class Student(Person):
    def get_role(self):
        return f"{self.name} is a Student"

class School:
    def __init__(self):
        self.members = []

    def add_member(self, person):
        self.members.append(person)

    def show_roles(self):
        for member in self.members:
            print(member.get_role())

school = School()
school.add_member(Teacher("Alice"))
school.add_member(Student("Bob"))
school.show_roles()
