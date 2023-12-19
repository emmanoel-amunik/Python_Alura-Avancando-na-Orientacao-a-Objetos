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

    def __str__(self):
        return f"{self._name} - {self.year} - {self._likes}"


class Movie(Program):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    def __str__(self):
        return f"{self._name} - {self.year} - {self.duration} - {self._likes}"


class Serie(Program):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        return f"{self._name} - {self.year} - {self.seasons} - {self._likes}"


avengers = Movie("avengers: infinity war", 2018, 160)
atlanta = Serie("atlanta", 2018, 2)

avengers.give_likes()
atlanta.give_likes()
atlanta.give_likes()

movies_n_series = [avengers, atlanta]

for item in movies_n_series:
    print(item)
