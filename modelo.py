class Movie:
    def __init__(self, name, year, duration):
        self.__name = name.title()
        self.year = year
        self.duration = duration
        self.__likes = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name.titlle()

    @property
    def likes(self):
        return self.__likes

    def give_likes(self):
        self.__likes += 1


class Serie:
    def __init__(self, name, year, seasons):
        self.__name = name.title()
        self.year = year
        self.seasons = seasons
        self.__likes = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name.titlle()

    @property
    def likes(self):
        return self.__likes

    def give_likes(self):
        self.__likes += 1


avengers = Movie("avengers: infinity war", 2018, 160)
avengers.give_likes()
print(f"Name: {avengers.name} - Year: {avengers.year} "
      f"- Duration: {avengers.duration} - Likes: {avengers.likes}")


atlanta = Serie("atlanta", 2018, 2)
atlanta.give_likes()
atlanta.give_likes()
print(f"Name: {atlanta.name} - Year: {atlanta.year} "
      f"- Seasons: {atlanta.seasons} - Likes: {atlanta.likes}")
