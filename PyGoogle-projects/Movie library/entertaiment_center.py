import fresh_tomatoes
import media

toy_story = media.Movie('Toy Story',
                        'A story of a boy and his toys that come to life',
                        'https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-12561-wt2it4_fbf729c8.jpeg?region=0,0,300,450',
                        'https://www.youtube.com/watch?v=JcpWXaA2qeg')
#print(toy_story.storyline)
    
avatar = media.Movie('Avatar',
                     'A marine on a alien planet',
                     'https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg',
                     'https://www.youtube.com/watch?v=5PSNL1qE6VY')
#print(avatar.storyline)
#avatar.show_trailer()

interstellar = media.Movie('Interstellar',
                           'Time travelig in space',
                           'https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_UY1200_CR69,0,630,1200_AL_.jpg',
                           'https://www.youtube.com/watch?v=0vxOhd4qlnA')

ex_machina = media.Movie('Ex Machina',
                         'AI who is create to brake Turing"s test',
                         'https://images-na.ssl-images-amazon.com/images/M/MV5BMTUxNzc0OTIxMV5BMl5BanBnXkFtZTgwNDI3NzU2NDE@._V1_UY1200_CR90,0,630,1200_AL_.jpg',
                         'https://www.youtube.com/watch?v=EoQuVnKhxaM')

snowden = media.Movie('Snowden',
                      'Edward Snowden"s life',
                      'http://static.rogerebert.com/uploads/movie/movie_poster/snowden-2016/large_e5vQ0HztqucuLn2FK80QD2GSkfc.jpg',
                      'https://www.youtube.com/watch?v=QlSAiI3xMh4')

imitation_game = media.Movie('Imitation game',
                             'Alan Turing"s machine which decrypt code',
                             'http://www.cinefish.bg/data/movies_images/244/p_244136.jpg',
                             'https://www.youtube.com/watch?v=S5CjKEFb-sM')
movies = [toy_story, avatar, interstellar, ex_machina, snowden, imitation_game]
fresh_tomatoes.open_movies_page(movies)


#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)



