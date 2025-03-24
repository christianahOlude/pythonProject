
from datetime import datetime
class Movie:
    def __init__(self, movie_title):
        self.movie_title = movie_title
        # self.movies:{movies} = movies
        self.rating = []
        self.is_created = datetime.now()

    def set_movie_title(self, movie_title):
        self.movie_title = movie_title

    def get_movie_title(self):
        return self.movie_title

    def set_rating(self, rating):
        self.rating.append(rating)

    def get_rating(self):
        return self.rating

    def get_is_created(self):
        return self.is_created


