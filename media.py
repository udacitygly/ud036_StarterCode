class Movie():
    """ This class is an abstraction of a movie with variety of attributes """
    def __init__(self, a_title, a_story_line, a_poster_image, a_trailer):
        """ Creates object with title, storyline, and URL for poster and trailer

        Attributes:
        a_title (str): The exact title of the movie
        a_storyline (str): Short description of the movie
        a_poster_image (str): Exact URL to image file with movie poster
        a_trailer (str): Exact URL to YouTube video
        """
        self.title = a_title
        self.story_line = a_story_line
        self.poster_image_url = a_poster_image
        self.trailer_youtube_url = a_trailer
        