from media_class import Media

class Movie(Media):
    def __init__(self, poster_link, title, released_year, certificate, runtime, genre, IMDB_rating, overview, meta_score, director, Star1, Star2, Star3, Star4):
        super().__init__(poster_link, title, certificate, genre, IMDB_rating, overview, meta_score, director, Star1, Star2, Star3, Star4)
        self.release = released_year
        self.mruntime = runtime
        self.cast = [Star1,Star2,Star3,Star4]
        
