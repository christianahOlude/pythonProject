from classwork.movieapp import movieapp


def main():
    messages = """
        ~~~ Welcome to Bad movie app ~~~
        1. Add a Movie
        2. Rate a Movie
        3. Check average rating of a Movie
        4. Check average rating of Movies
        5. Exit the program
        Enter your choice: 
    """

    while True:
        input_message = input(messages)
        match input_message:
            case "1":
                try:
                    movie_name = input("Enter the movie name: ")
                    movies = movieapp.MovieApp()
                    response = movies.add_movie(movie_name)
                    print(f" {response} has been added")
                except TypeError as e:
                    print(e)


            case "2":
                try:
                    movie_name = input("Enter the movie name: ")
                    rate = input("Enter your rate: ")
                    movies = movieapp.MovieApp()
                    # movie = movieapp.Movie(movie_name)
                    movies.add_movie(movie_name)
                    movies.rate_movie(movie_name,rate)
                    print(f" {movie_name} now has {rate} rating")
                except TypeError as e:
                    print(e)


            case "3":
                movie_name = input("Enter the movie name: ")
                movies = movieapp.MovieApp()
                print(movies.average_rating(movie_name))


            case "4":
                main()

            case "5":
                exit(0)

main()
if __name__ == "__main__":
    main()
