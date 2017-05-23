# UdacityMovieTrailerProject

Hi, welcome to my first Python project! I changed a little the scope of the project in a away to use API integration, Bootstrap and Django. After trying 3 times to have the project reviewed using Flask I decided to rewrite using Django that I read the documentation deeper and have more control about starting a new project and using the features that I need.

This project was developed using Python 3.6.1. Remember to have this version installed.

As I'm using TMDB database API to download your favorite movies, I left my credentials in the my_setup = TMDB_Setup() in tmdb.py file in order to make the evaluation easy. Don't worry about having a new registration on TMDB website.

The project was tested in local server.

Follow the steps to test the app:
1) Setup Python 3.6.1 enviroment (https://docs.python.org/3/using/)
2) Remember to run: pip install -r requirements.txt
3) Check the files:
    movies.py -> Build the favorite movie array to be used in our HTML page
    tmdb.py -> Connect with TMDB API, authenticate and retrieve data
4) Open cmd.exe or similar command shell with super user permission
5) Go to ~/UdacityMovieTrailerProject/MovieTrailerWebsite/
6) Run the command: python manage.py runserver
7) Open the URL displayed in the command shell. In my localserver was: http://127.0.0.1:8000/

Hope that works!
