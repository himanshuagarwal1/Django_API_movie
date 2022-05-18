
from marshmallow import validate
from marshmallow import fields
from marshmallow import Schema
from marshmallow.decorators import post_load

from techtest.movies.models import Movie
from techtest.comments.schemas import CommentSchema
from techtest.comments.models import Comment



class MovieSchema(Schema):
    class Meta(object):
        model = Movie

    id = fields.Integer()
    Title = fields.String()
    Year = fields.String()
    Rated = fields.String()
    Released = fields.String()
    Runtime = fields.String()
    Genre = fields.String()
    Director = fields.String()
    Writer = fields.String()
    Actors = fields.String()
    Plot = fields.String()
    Language = fields.String()
    Country  = fields.String()
    Awards  = fields.String()
    Poster = fields.String()
    
    Metascore = fields.String()
    imdbRating =fields.String()
    imdbVotes = fields.String()
    imdbID = fields.String()
    Type = fields.String()
    DVD = fields.String()
    BoxOffice = fields.String()
    Production = fields.String()
    Website = fields.String()
    Response = fields.String()
    Comments = fields.Method(
        required=False, serialize="get_comments", deserialize="load_comments"
    )

    def get_comments(delf, movies):
        
        return CommentSchema().dump(movies.Comments.all(), many=True)

    def load_comments(self, comments):
        
        return [
            Comment.objects.get_or_create(id = comment.pop("id", None), defaults=comment)[0]
            for comment in comments
        ]

    @post_load
    def update_or_create(self, data, *args, **kwargs):
        comments = data.pop("Comments", None)       
        
        
        movie, _ = Movie.objects.update_or_create(
            id=data.pop("id", None), defaults=data
        )
        if isinstance(comments, list):
            movie.comments.set(comments)
        return movie
