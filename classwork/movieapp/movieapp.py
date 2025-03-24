from classwork.movieapp.movie import Movie

class MovieApp:
    def __init__(self):
        # self.date = datetime
        self.movie = []
        self.rating = []

    def calculate_rating(self):
        total = sum(self.rating)
        return total / len(self.rating)

    def add_movie(self, movie_name):
        movie = Movie(movie_name)
        if len(movie_name.strip()) == 0:
            raise TypeError("Movie name cannot be None")
        for film in self.movie:
            if movie_name == film:
                raise TypeError("Movie name already exists")
            if movie_name == ' ':
                raise TypeError("Movie name is required")
        self.movie.append(movie_name)
        return movie.get_movie_title()

    def rate_movie(self, movie_name, rating):
        if movie_name not in self.movie:
            raise TypeError("Movie name not found")
        if movie_name == ' ':
            raise TypeError("Movie name is required")
        elif int(rating) > 5 or int(rating) < 0:
            raise TypeError("Rating must be between 0 and 5")
        else:
            self.rating.append(rating)
            return self.movie.index(movie_name)

    def average_rating(self, movie_name):
        if movie_name not in self.movie:
            raise TypeError("Movie name not found")
        else:
            total = sum(self.rating)
            return total / len(self.rating)

    # def general_average_rating(self,movie_name):
    #     for movie in self.movie:
