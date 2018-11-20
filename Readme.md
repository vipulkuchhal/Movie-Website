TITLE : MOVIE TRAILER
PYTHON VERSION : Python 2.7
PROJECT : A python file generating a movie website
CODE CHECKER: PEP8

Now to run the project we need to follow these steps:
1.Unzip the file.
2.Now list will be get displayed.
3.Go to the entertainment file and right click on the file.
4.Now click on the Edit with IDLE.
5.A python file will get displayed.
6.Now go to the run option and click on Run Module.
7.The webbrowser page will open and display the lsit of Trailers. 

Description: A server-side code that stores a list of movies, a movie trailer URL, and serve this data as web page; allowing visitors to review their movies and watch trailers.
In this readme file, I explain in detail how our website; fresh_tomatoes.py functions with media.py and entertainment.py to display trailer of movie.
Programming Foundations with Python
We started off with a plan:
1.	Go to the website
2.	See all of the movies displayed
3.	Click on one to play its trailer
Class structure
We will need classes to build this movie website. We want our Movie class to be a template for a generic movie, and then create instances of that class like this:
dangal= Movie()
and add details to each specific movie. So, we first need to come up with a list of properties that we think every movie should have:
1.	title
2.	trailer
3.	storyline
4.	poster_image
Defining our class
We created a file called media.py. Inside of it, start our Movie class by typing:
class Movie():
We Created a second file, called entertainment.py and connected it to the media.py file.
import media
dangal= media.Movie()
Let's define init. It will be defined like any other function in Python, and we use this with two underscore(__)before and after init.
And we define class movie like this:
class Movie():
    def __init__(self, title, storyline, poster_image, trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

Going back to our other file:
import media

dangal= media.Movie("Dangal","A Story of a two girls who made our India proud",
                     "https://goo.gl/FWuKtc",
                     "https://www.youtube.com/watch?v=x_7YlGv9u1g")

print (dangal.storyline)

What's going on behind the scenes?
When we run this code:
dangal= media.Movie() several things happen.
init gets called All references to self inside of init point to dangal. The variables associated with the instance dangal get assigned values:dangal.title becomes "Dangal" dangal.storyline becomes "A Story of a two girls who made our India proud".
The same is used to create the other movies like Sultan,Bajirao,Kaabil and 3 idiots

Showing Trailers
We defined our show_trailer method inside of the Movie class. Methods defined inside of a class are called instance methods.
import webbrowser

class Movie():
    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        webbrowser.open(self.trailer_url)
import media
dangal = media.Movie("Dangal",
                     "A Story of a two girls who made our India proud",
                     "https://goo.gl/FWuKtc",
                     "https://www.youtube.com/watch?v=x_7YlGv9u1g")


dangal.show_trailer()
The web browser should open with the trailer playing!
Creating the Movie Website
We used this file called fresh_tomatoes.py in our own entertainment code. Let's create a list of movies that we are going to use:
import fresh_tomatoes

movies = movies = [dangal, sultan, idiots, bahubali, bajirao, kaabil]
fresh_tomatoes.open_movies_page(movies)

