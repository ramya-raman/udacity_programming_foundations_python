import webbrowser

class Movie() :
    """This class provides a way to store movie related information"""
    
    VALID_RATINGS = ["G" , "PG" , "PG-13" , "R"]    
    def __init__(movie, movie_title, movie_storyline, poster_image, trailer_youtube) :
        movie.title = movie_title
        movie.storyline = movie_storyline
        movie.poster_image_url = poster_image
        movie.trailer_youtube_url = trailer_youtube

    def show_trailer(self) :
        webbrowser.open(self.trailer_youtube_url)
