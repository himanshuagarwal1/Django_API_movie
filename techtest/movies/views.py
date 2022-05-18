
import json

import requests

from marshmallow import ValidationError
from django.views.generic import View

from techtest.movies.models import Movie
from techtest.movies.schemas import MovieSchema
from techtest.utils import json_response


class MoviesListView(View):
    def get(self, request, *args, **kwargs):
        return json_response(MovieSchema().dump(Movie.objects.all(), many=True))

    def post(self, request, *args, **kwargs):
        x = json.loads(request.body)
        
        if x["title"] == None or x["title"] == "":
            return json_response("no title found", 404)
        URL = "http://www.omdbapi.com/?i=tt3896198&apikey=f98c6630"
        response = requests.get(URL, {"t":x["title"]})
        data = response.json()
        del data["Ratings"]  
        try:           
            movie = MovieSchema().load(data)            
        except ValidationError as e:
            return json_response(e.messages, 400)
        return json_response(MovieSchema().dump(movie), 201)


class MovieView(View):
    def dispatch(self, request, movie_id, *args, **kwargs):
        try:
            self.movie = Movie.objects.get(pk=movie_id)
        except Movie.DoesNotExist:
            return json_response({"error": "No Movie matches the given query"}, 404)
        self.data = request.body and dict(json.loads(request.body), id=self.movie.id)
        return super(MovieView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return json_response(MovieSchema().dump(self.movie))

    def put(self, request, *args, **kwargs):
        try:
            self.Movie = MovieSchema().load(self.data)
        except ValidationError as e:
            return json_response(e.messages, 400)
        return json_response(MovieSchema().dump(self.Movie))

    def delete(self, request, *args, **kwargs):
        self.Movie.delete()
        return json_response()
