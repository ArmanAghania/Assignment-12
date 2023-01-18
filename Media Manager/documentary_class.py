from media_class import Media

class Documentary(Media):
    def __init__(self, poster_link, title, certificate, genre, IMDB_rating, overview, meta_score, director, Star1, Star2, Star3, Star4):
        super().__init__(poster_link, title, certificate, genre, IMDB_rating, overview, meta_score, director, Star1, Star2, Star3, Star4)
        