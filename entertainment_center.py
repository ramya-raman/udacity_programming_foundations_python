import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                  "A story of a boy and his toys that come to life",
                  "https://upload.wikimedia.org/wikipedia/sco/1/13/Toy_Story.jpg",
                  "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.storyline)

avatar = media.Movie("Avatar" , "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/sco/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)
#avatar.show_trailer()


despicable_me = media.Movie("Despicable Me", "A supervillain becomes superdad" ,
                            "https://upload.wikimedia.org/wikipedia/sco/d/db/Despicable_Me_Poster.jpg",
                            "https://www.youtube.com/watch?v=sUkZFetWYY0")
#despicable_me.show_trailer()

megamind = media.Movie("Megamind", "A supervillain creates a superhero who become evil",
                       "https://upload.wikimedia.org/wikipedia/en/8/89/Megamind2010Poster.jpg",
                       "https://www.youtube.com/watch?v=NPI0eatlo_M")

minions = media.Movie("Minions", "Minions decidde to find a new master",
                      "https://upload.wikimedia.org/wikipedia/en/3/3d/Minions_poster.jpg",
                      "https://www.youtube.com/watch?v=P9-FCC6I7u0")
good_dinosaur = media.Movie("The Good Dinosaur", "A dinosaur with a human friend",
                            "https://upload.wikimedia.org/wikipedia/en/8/80/The_Good_Dinosaur_poster.jpg",
                            "https://www.youtube.com/watch?v=O-RgquKVTPE")

movies = [toy_story, avatar, despicable_me, megamind, minions, good_dinosaur]
fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.__doc__)
