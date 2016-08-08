import webbrowser


class Video():
    """This class provides overarching structure for any type of video"""
    def __init__(self,title,duration):
        self.title = title
        self.duration = duration
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


        
class Movie(Video):
    """This class povides a way to store movies and related info"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    def __init__(self, movie_title, duration, movie_storyline, poster_image,trailer_youtube):
        Video.__init__(self,movie_title,duration)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube


class Tv_show(Video):
    def __init__(self, title, duration, storyline,poster_image,trailer_youtube):
        Video.__init__(self,title,duration)
        self.storyline = storyline
        self.poster_image = poster_image
        self.trailer_youtube = trailer_youtube
