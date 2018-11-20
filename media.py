import webbrowser  # importing webbrowser library


class Movie():
    """This class provides a way to store movie related info"""

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """calling init function in python and storing values of
           movie variables using self which is a predefined in __init__"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """this function opens the youtube url to display trailer of movie"""
        webbrowser.open(self.trailer_youtube_url)
