import webbrowser

class Movie():
    """ this class is parent class which provide the information related to video."""    

    # init method is a constructor that initializes the data.
    # self is the instance(like alaska,bfg,starwar,american_sniper)
    # there are 3 arguments- title, duration and quality. They are instance variable"""
    

    def __init__(temp, movie_title, movie_overview, poster_image, trailer_youtube):
        """ this method is constructor for initialize the values of parent class"""
        temp.title = movie_title
        temp.movie_overview = movie_overview
        temp.poster_image_url = poster_image
        temp.trailer_youtube_url = trailer_youtube

    def show_trailer(temp):
        """ it will take instance of Movie classs and show the trailer of that instance"""
        webbrowser.open(temp.trailer_youtube_url)
