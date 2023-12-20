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


class Playlist:
    def __init__(self, name, programs):
        self.name = name
        self._programs = programs

    def __getitem__(self, p_item):
        return self._programs[p_item]

    @property
    def listing(self):
        return self._programs

    def __len__(self):
        return len(self._programs)


avengers = Movie("avengers: infinity war", 2018, 160)
atlanta = Serie("atlanta", 2018, 2)
scary = Movie("Scary Movie", 1999, 100)
daredevil = Serie("daredevil", 2016, 2)


daredevil.give_likes()
daredevil.give_likes()
avengers.give_likes()
atlanta.give_likes()
atlanta.give_likes()
atlanta.give_likes()
atlanta.give_likes()
scary.give_likes()
scary.give_likes()
scary.give_likes()


movies_n_series = [avengers, atlanta, daredevil, scary]
weekend_playlist = Playlist("Weekend", movies_n_series)

print(f"Size of the playlist: {len(weekend_playlist)}")

print(weekend_playlist[0])

for item in weekend_playlist:
    print(item)
