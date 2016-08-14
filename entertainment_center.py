import media
import fresh_tomatoes
##This file contains the objects for each movie initiated by media.py.
## Each object contains the movie title, duration, short description,...
## link to the poster, and a link to the youtube trailer.

shawshank = media.Movie("Shawshank Redemption",120,"Victory over actual prison",
                        "https://www.movieposter.com/posters/archive/main/42/MPW-21321",
                        "https://www.youtube.com/watch?v=6hB3S9bIaco")
office_space = media.Movie("Office Space",120,"Victory over cubicle prison",
                        "https://www.movieposter.com/posters/archive/main/58/MPW-29049",
                           "https://www.youtube.com/watch?v=dMIrlP61Z9s")
citizen_four = media.Movie("Citizen Four",120,"Victory over over-reach",
                        "http://www.impawards.com/2014/posters/citizenfour.jpg",
                           "https://www.youtube.com/watch?v=rHaWhUjV96M")
step_brothers = media.Movie("Step Brothers",120,"Prestige...World Wide.",
                        "http://www.impawards.com/2008/posters/step_brothers.jpg",
                           "https://www.youtube.com/watch?v=V6Z7PEvedHQ")


movies = [shawshank,office_space,citizen_four,step_brothers]
fresh_tomatoes.open_movies_page(movies)

print(media.Movie.__module__)
print(media.Movie.__name__)
