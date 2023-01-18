class Media:
    def __init__(self, poster_link, title, certificate, genre, IMDB_rating, overview, meta_score, director, Star1, Star2, Star3, Star4):
        self.poster = poster_link
        self.title = title
        self.cert = certificate
        self.genre = genre
        self.rate = IMDB_rating
        self.overview = overview
        self.meta = meta_score
        self.director = director
        self.star1 = Star1
        self.star2 = Star2
        self.star3 = Star3
        self.star4 = Star4
        self.cast = [self.star1,self.star2,self.star3,self.star4]
    @staticmethod
    def show_info(self):
        #p = self.poster
        t = self.title
        c = self.cert
        g = self.genre
        r = self.rate
        o = self.overview
        m = self.meta
        d = self.director
        s = self.cast
        print(t,c,g,r,o,m,d,s)
        

    def download(self):
        ...

    
