import media  # here importing media library
import fresh_tomatoes  # importing fresh tomatoes

# storing information in variable dangal
dangal = media.Movie("Dangal",
                     "A Story of a two girls who made our India proud",
                     "https://goo.gl/FWuKtc",
                     "https://www.youtube.com/watch?v=x_7YlGv9u1g")

# output the value of dangal storyline
print(dangal.storyline)

# storing information in variable sultan
sultan = media.Movie("Sultan", "A story of self motivated man",
                     "https://goo.gl/UUWjLd",
                     "https://www.youtube.com/watch?v=wPxqcq6Byq0")

# output the value of sultan storyline
print(sultan.storyline)

# storing information in variable idiots
idiots = media.Movie("3 Idiots", "A story of 3 friends",
                     "https://goo.gl/onwNCy",
                     "https://www.youtube.com/watch?v=K0eDlFX9GMc")

# output the value of idiots storyline
print(idiots.storyline)

# storing information in variable bahubali
bahubali = media.Movie("Bahubali", "A story of Warrior",
                       "https://goo.gl/9rttPG",
                       "https://www.youtube.com/watch?v=VdafjyFK3ko")

# output the value of bahubali storyline
print(bahubali.storyline)

# storing information in variable bajirao
bajirao = media.Movie("Bajirao Mastani", "A story of Maharashtaran Peshwa",
                      "https://goo.gl/AMxZSw",
                      "https://www.youtube.com/watch?v=Nbj01wzrfYA")

# output the value of bajirao storyline
print(bajirao.storyline)

# storing information in variable kaabil
kaabil = media.Movie("Kaabil", "A story of Blind Man",
                     "https://goo.gl/YkXuRF",
                     "https://www.youtube.com/watch?v=nubDFeiUAsI")

# output the value of kaabil storyline
print(kaabil.storyline)

# an array of given movies
movies = [dangal, sultan, idiots, bahubali, bajirao, kaabil]

# calling fresh_tomatoes library to display information
fresh_tomatoes.open_movies_page(movies)

# output the movie document
print(media.Movie.__doc__)
