#!/usr/bin/env python
# -*- coding: utf-8 -*-

import http.client
import json


class Default(dict):
    """Class to be used with format_map."""

    def __missing__(self, key):
        """Correction __missing__ the code."""
        return key


class TMDB_Setup():
    """The Movie Database setup params."""

    def __init__(self, Username, Password):
        """How to initilialize the class."""
        self.appAPIKEY = "6a916bd6117299211ce7d825307e6c82"
        self.Username = Username
        self.Password = Password


# Command to setup and connect to TMDB
my_setup = TMDB_Setup("victorbarros", "udacity2017")
conn = http.client.HTTPSConnection("api.themoviedb.org")


class TMDB_Request_Token(TMDB_Setup):
    """Request a new token to be used to validate the token."""

    def __init__(self):
        """Request a new token to be used to validate the token."""
        payload = "{}"
        url = "/3/authentication/token/new?api_key={api_key}"
        url = url.format_map(Default(api_key=my_setup.appAPIKEY))
        print("[TMDB_Request_Token] Call URL in: " + url)
        conn.request("GET", url, payload)
        res = conn.getresponse()
        raw_data = res.read()
        data = json.loads(raw_data)
        print(raw_data)
        self.RequestToken = data['request_token']


class TMDB_Validade_Token(TMDB_Setup):
    """Validate the new token."""

    def __init__(self, rt):
        """Validate the new token."""
        payload = "{}"
        url = "/3/authentication/token/validate_with_login?request_token={request_token}&password={password}&username={username}&api_key={api_key}"
        url = url.format_map(Default(request_token=rt, password=my_setup.Password, username=my_setup.Username, api_key=my_setup.appAPIKEY))
        print("[TMDB_Validade_Token] Call URL in: " + url)
        conn.request("GET", url, payload)
        res = conn.getresponse()
        raw_data = res.read()
        data = json.loads(raw_data)
        print(raw_data)
        # Check if exist any status message or error message
        if not str(raw_data).find("status_message") == -1:
            print(data['status_message'])
            self.ValidatedToken = False
        else:
            if data['success'] is True:
                self.ValidatedToken = data['success']
            else:
                self.ValidatedToken = False


class TMDB_CreateSession(TMDB_Setup):
    """Create TMDB session."""

    def __init__(self, rt):
        """Create TMDB session."""
        payload = "{}"
        url = "/3/authentication/session/new?api_key={api_key}&request_token={request_token}"
        url = url.format_map(Default(api_key=my_setup.appAPIKEY, request_token=rt))
        print("[TMDB_CreateSession] Call URL in: " + url)
        conn.request("GET", url, payload)
        res = conn.getresponse()
        raw_data = res.read()
        data = json.loads(raw_data)
        print(raw_data)
        # Check if exist any status message or error message
        if not str(raw_data).find("status_message") == -1:
            print(data['status_message'])
            self.ValidatedSession = False
        else:
            if data['success'] is True:
                self.ValidatedSession = data['success']
                self.SessionID = data['session_id']
            else:
                self.ValidatedSession = False


class TMDB_GetAccountID(TMDB_Setup):
    """Get the account ID to be used by other requests."""

    def __init__(self, sid):
        """Get the account ID to be used by other requests."""
        payload = "{}"
        url = "/3/account?api_key={api_key}&session_id={session_id}"
        url = url.format_map(Default(api_key=my_setup.appAPIKEY, session_id=sid))
        print("[TMDB_GetAccountID] Call URL in: " + url)
        conn.request("GET", url, payload)
        res = conn.getresponse()
        raw_data = res.read()
        data = json.loads(raw_data)
        print(raw_data)
        # Check if exist any status message or error message
        if not str(raw_data).find("status_message") == -1:
            print(data['status_message'])
            self.AccountID = 0
        else:
            self.AccountID = data['id']
            print("Account ID defined in " + str(self.AccountID))


class TMDB_FavoriteMovies(TMDB_Setup):
    """Get the list of Favorite Movies."""

    def __init__(self, sid, acid):
        """Get the list of Favorite Movies."""
        payload = "{}"
        url = "/3/account/{account_id}/favorite/movies?api_key={api_key}&session_id={session_id}"
        url = url.format_map(Default(account_id=acid, api_key=my_setup.appAPIKEY, session_id=sid))
        print("[TMDB_FavoriteMovies] Call URL in: " + url)
        conn.request("GET", url, payload)
        res = conn.getresponse()
        raw_data = res.read()
        data = json.loads(raw_data)
        print(raw_data)
        # Check if exist any status message or error message
        if not str(raw_data).find("status_message") == -1:
            print(data['status_message'])
        else:
            if data['page'] == 1:
                self.MovieList = data
            else:
                self.MovieList = None


class TMDB_Trailer(TMDB_Setup):
    """Get the movie trailer."""

    def __init__(self, mid):
        """Get the movie trailer."""
        payload = "{}"
        url = "/3/movie/{movie_id}/videos?api_key={api_key}"
        url = url.format_map(Default(movie_id=mid, api_key=my_setup.appAPIKEY))
        print("[TMDB_Trailer] Call URL in: " + url)
        conn.request("GET", url, payload)
        res = conn.getresponse()
        raw_data = res.read()
        data = json.loads(raw_data)
        print(raw_data)
        # Check if exist any status message or error message
        if not str(raw_data).find("status_message") == -1:
            print(data['status_message'])
        else:
            if data['id'] > 0:
                self.TrailerList = data
            else:
                self.TrailerList = None
