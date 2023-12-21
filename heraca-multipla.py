class Employer:
    def __init__(self, name):
        self.name = name

    def hours_register(self, hours):
        print("Hours registered...")

    def display_tasks(self):
        print("Did a lot of things...")


class Caelum(Employer):
    def display_tasks(self):
        print("Did a lot of things, Caelum...")

    def search_courses_of_the_month(self, month=None):
        print(f"Displaying courses - {month}" if month else
              "Displaying the courses of this month")


class Alura(Employer):
    def display_tasks(self):
        print("Dis a lot of things, Alura!")

    def search_questions_without_answers(self):
        print("Displaying unanswered questions in the forum")


class Hipster:
    def __str__(self):
        return f"Hipster, {self.name}"

class Junior(Alura):
    pass


class Pleno(Alura, Caelum):
    pass


class Senior(Alura, Caelum, Hipster):
    pass


marco = Senior('Marco')
print(marco)
# MRO
# Pleno > Alura > Employer > Caelum > Employer

