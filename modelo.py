class Program:
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name.titlle()

    @property
    def likes(self):
        return self._likes

    def give_likes(self):
        self._likes += 1


class Movie(Program):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration


class Serie(Program):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons


avengers = Movie("avengers: infinity war", 2018, 160)
avengers.give_likes()
print(f"{avengers.name} - {avengers.duration} - {avengers.likes}")


atlanta = Serie("atlanta", 2018, 2)
atlanta.give_likes()
atlanta.give_likes()
print(f"{atlanta.name} - {atlanta.seasons} - {atlanta.likes}")
