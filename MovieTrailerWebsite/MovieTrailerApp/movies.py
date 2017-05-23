#!/usr/bin/env python
# -*- coding: utf-8 -*-
from MovieTrailerApp import tmdb
import json


class OpenFavoriteListMovie():
    """
    This class is responsible to create the favorite movie list.

    Use TMDB API.
    """

    def __init__(self):
        """Request a valid token to connect the API."""
        rt = tmdb.TMDB_Request_Token()
        vt = tmdb.TMDB_Validade_Token(rt.RequestToken)
        if vt.ValidatedToken is True:
            cs = tmdb.TMDB_CreateSession(rt.RequestToken)
            """With the API validated, it is necessary to start a session
            to read some information"""
            if cs.ValidatedSession is True:
                print("Sessão validada com token "+rt.RequestToken+" e sessão criada com ID "+cs.SessionID)
                acid = tmdb.TMDB_GetAccountID(cs.SessionID)
                """Check if there is any authentication made ID diff 0"""
                if not acid.AccountID == 0:
                    """With the session validated, it is time to
                    build the favorite movie list"""
                    tmfl = tmdb.TMDB_FavoriteMovies(cs.SessionID, acid.AccountID)
                    dataFavMovies = tmfl.MovieList
                    movies_list = []
                    """Build the output array to be used in our HTML page"""
                    for i in dataFavMovies['results']:
                        movies_dict = {}
                        movies_dict['original_title'] = i['original_title']
                        movies_dict['poster_path'] = "https://image.tmdb.org/t/p/w150_and_h225_bestv2/"+i['poster_path']
                        movies_dict['overview'] = i['overview']
                        movies_dict['id'] = i['id']
                        trailer = tmdb.TMDB_Trailer(i['id'])
                        dataFavMovieTrailers = trailer.TrailerList
                        trailer_list = []
                        """Build the sub-array Trailers to
                        be used in our HTML page"""
                        for t in dataFavMovieTrailers['results']:
                            trailer_dict = {}
                            trailer_dict['url'] = "https://www.youtube.com/watch?v="+t['key']
                            trailer_dict['trailer_name'] = t['name']
                            trailer_list.append(trailer_dict)
                        movies_dict['trailers'] = trailer_list
                        movies_list.append(movies_dict)
                    """Return the array to be used at our HTML page"""
                    self.FavoriteMovieData = json.dumps(movies_list, ensure_ascii=False)
                else:
                    print("Account not valid")
            else:
                print("Session not valid")
        else:
            print("Token is not valid")
