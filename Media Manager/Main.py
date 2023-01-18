from media_class import Media
from movie_class import Movie
from series_class import Series
from documentary_class import Documentary
from short_clip_class import Short_Clip
import pandas as pd


Moviesdb = []
Seriesdb = []
def read_from_database():
    df1 = pd.read_csv('Media/imdb_top_1000.csv')

    for i in range (1000):
        result = df1.iloc[i]
        my_obj = Movie(result[0],result[1],result[2],result[3],result[4],result[5],result[6],result[7],result[8],result[9],result[10],result[11],result[12],result[13])

        Moviesdb.append(my_obj)
    
    

    
    # df2 = pd.read_csv('Media/series_data.csv')
    # df2['Certificate'].fillna('Not Entered')

    # print(df2.info())
    # for i in range(1000):
    #     result = df2.iloc[i]
    #     my_obj = Series(result[0],result[1],result[2],result[3],result[4],result[5],result[6],result[7],result[8],result[9],result[10],result[11])
    #     Seriesdb.append(my_obj)
    
    # df3 = df2[:1000][:]
    # print(df3.drop('No_of_Votes',axis=1))
    



read_from_database()
print('Welcome to the Media Market')
print('''
1. search
2.exit
''')
command = input('What do you want to do?! ')

while True:
    if int(command) == 1:
        search_term = input('Enter the movie\'s name you are looking for: ')
        try:
            for Movie in Moviesdb:
                if Movie.title == search_term:
                    Movie.show_info()
        except:
            print('Movie not Found')

    elif int(command) == 2:
        exit(0)
        
    else:
        print('Command entered is wrong')