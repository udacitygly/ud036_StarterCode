import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A Story of a boy and toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

matrix = media.Movie("The Matrix",
                        "Man stops living life as a battery",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/c/c1/The_Matrix_Poster.jpg/220px-The_Matrix_Poster.jpg",
                        "https://www.youtube.com/watch?v=m8e-FF8MsqU")

terminator = media.Movie("Terminator",
                        "Life tale of a bad robot",
                        "https://upload.wikimedia.org/wikipedia/en/7/70/Terminator1984movieposter.jpg",
                        "https://www.youtube.com/watch?v=k64P4l2Wmeg")

wonder_woman = media.Movie("Wonder Woman",
                        "Origin story of superhero known as Wonder Woman",
                        "https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg",
                        "https://www.youtube.com/watch?v=1Q8fG0TtVAY")

jumanji = media.Movie("Jumanji",
                        "A Story a video game that comes to life",
                        "https://upload.wikimedia.org/wikipedia/en/d/dc/Jumanji_Welcome_to_the_Jungle.png",
                        "https://www.youtube.com/watch?v=5p18zqZmeiI")
star_wars = media.Movie("Star Wars",
                        "A story of a Dad that is very mean while in space",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/8/87/StarWarsMoviePoster1977.jpg/220px-StarWarsMoviePoster1977.jpg",
                        "https://www.youtube.com/watch?v=XHk5kCIiGoM")
                        
movies = [toy_story, matrix, terminator, wonder_woman, jumanji, star_wars]
fresh_tomatoes.open_movies_page(movies)

