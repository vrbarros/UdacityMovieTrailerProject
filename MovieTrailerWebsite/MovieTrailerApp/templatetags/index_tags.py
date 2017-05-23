from django import template
from MovieTrailerApp import movies
import json

register = template.Library()


@register.assignment_tag
def get_movies():
    """Retrieve the movie list from the movie class."""
    fvml = movies.OpenFavoriteListMovie()
    print("[JSON]->"+fvml.FavoriteMovieData)
    return json.loads(fvml.FavoriteMovieData)
