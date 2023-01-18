from media_class import Media


class Series(Media):
    def __init__(self, poster_link, title,runtime_series, certificate, runtime_episodes, genre, IMDB_rating, overview, Star1, Star2, Star3, Star4):
        super().__init__(self, poster_link, title,runtime_series, certificate, runtime_episodes, genre, IMDB_rating, overview, Star1, Star2, Star3, Star4)

        self.sruntime = runtime_series
        self.eruntime = runtime_episodes