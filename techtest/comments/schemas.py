
from marshmallow import validate
from marshmallow import fields
from marshmallow import Schema
from marshmallow.decorators import post_load
from techtest.movies.models import Movie
from techtest.comments.models import Comment

class CommentSchema(Schema):
    class Meta(object):
        model = Comment

    id = fields.Integer()   
    Comments = fields.String()

     

    @post_load
    def update_or_create(self, data, *args, **kwargs):
               
        comment, _ = Comment.objects.update_or_create(
            id=data.get("id"), defaults=data  )
        
        
        movie = Movie.objects.get(id=data["id"])
        
        movie.Comments.add(comment)
       
        return comment
