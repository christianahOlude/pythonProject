from unittest import TestCase

from classwork.movieapp.movie import Movie
from classwork.movieapp.movieapp import MovieApp


class TestAddAndRateMovie(TestCase):
    # def setUp(self):
    #     self.movie = Movie()

    def test_that_movie_can_be_added(self):
        movie = MovieApp()
        self.assertEqual("Koto aye",movie.add_movie("Koto aye"))

    def test_that_movie_input_is_correct(self):
        movie = MovieApp()
        movie.add_movie("Koto aye")
        with self.assertRaises(TypeError):
            movie.add_movie(" ")


    def test_that_one_movie_cant_be_added_twice(self):
        movie = MovieApp()
        movie.add_movie("Koto aye")
        with self.assertRaises(TypeError):
            movie.add_movie("Koto aye")

    def test_that_more_than_one_movie_can_be_added(self):
        movie = MovieApp()
        self.assertEqual("Koto aye",movie.add_movie("Koto aye"))
        self.assertEqual("Chicken babe", movie.add_movie("Chicken babe"))
        self.assertEqual("Dark nuns", movie.add_movie("Dark nuns"))


    def test_that_movie_can_be_rated(self):
        movie = MovieApp()
        movie.add_movie("Koto aye")
        movie.add_movie("Chicken babe")
        movie.add_movie("Dark nuns")
        self.assertEqual(0,movie.rate_movie("Koto aye",2))
        self.assertEqual(1,movie.rate_movie("Chicken babe",3))


    def test_that_movie_is_in_the_list(self):
        movie = MovieApp()
        movie.add_movie("Koto aye")
        with self.assertRaises(TypeError):
            movie.rate_movie("Chicken babe",3)

    def test_that_rating_input_is_correct(self):
        movie = MovieApp()
        with self.assertRaises(TypeError):
            movie.rate_movie("Koto aye",9)

    def test_that_rating_input_not_lesser_than_1(self):
        movie = MovieApp()
        with self.assertRaises(TypeError):
            movie.rate_movie("Koto aye",-3)

    def test_that_movie_rating_average_can_be_checked(self):
        movie = MovieApp()
        movie.add_movie("Koto aye")
        movie.add_movie("Chicken babe")
        movie.add_movie("Dark nuns")
        self.assertEqual(0, movie.rate_movie("Koto aye", 2))
        self.assertEqual(0,movie.rate_movie("Koto aye",3))
        self.assertEqual(0, movie.rate_movie("Koto aye", 1))
        self.assertEqual(0, movie.rate_movie("Koto aye", 2))

        self.assertEqual(2,movie.calculate_rating())

    def test_that_movie_rating_average_input_is_correct(self):
        movie = MovieApp()
        with self.assertRaises(TypeError):
            movie.average_rating("")

    def test_that_all_movies_ratings_average_can_be_checked(self):
        movie = MovieApp()
        movie.add_movie("Koto aye")
        movie.add_movie("Chicken babe")
        movie.add_movie("Dark nuns")
        self.assertEqual(0, movie.rate_movie("Koto aye", 2))
        self.assertEqual(0, movie.rate_movie("Koto aye", 3))
        self.assertEqual(0, movie.rate_movie("Koto aye", 1))
        self.assertEqual(0, movie.rate_movie("Koto aye", 2))

        self.assertEqual(2, movie.calculate_rating())

        self.assertEqual(1, movie.rate_movie("Chicken babe", 2))
        self.assertEqual(1, movie.rate_movie("Chicken babe", 2))
        self.assertEqual(1, movie.rate_movie("Chicken babe", 4))
        self.assertEqual(1, movie.rate_movie("Chicken babe", 4))

        self.assertEqual(3,movie.calculate_rating())

        self.assertEqual(2, movie.rate_movie("Dark nuns", 2))
        self.assertEqual(2, movie.rate_movie("Dark nuns", 3))
        self.assertEqual(2, movie.rate_movie("Dark nuns", 5))
        self.assertEqual(2, movie.rate_movie("Dark nuns", 4))

        self.assertEqual(4, movie.calculate_rating())

    def test_that_all_movie_rating_average_input_is_correct(self):
        movie = MovieApp()
        with self.assertRaises(TypeError):
            movie.average_rating("")



