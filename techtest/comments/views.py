

import json
# Create your views here.

from marshmallow import ValidationError
from django.views.generic import View
from techtest.comments.models import Comment

from techtest.comments.schemas import CommentSchema
from techtest.utils import json_response


class CommentsListView(View):
    def get(self, request, *args, **kwargs):
        return json_response(CommentSchema().dump(Comment.objects.all(), many=True))

    def post(self, request, *args, **kwargs):
      
        try:            
            comment = CommentSchema().load(json.loads(request.body))
        except ValidationError as e:
            return json_response(e.messages, 400)
        return json_response(CommentSchema().dump(comment), 201)


class CommentView(View):
    def dispatch(self, request, comment_id, *args, **kwargs):
        try:
            self.comment = Comment.objects.get(pk=comment_id)
        except Comment.DoesNotExist:
            return json_response({"error": "No Comment matches the given query"}, 404)
        self.data = request.body and dict(json.loads(request.body), id=self.comment.id)
        return super(CommentView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return json_response(CommentSchema().dump(self.comment))

    def put(self, request, *args, **kwargs):
        try:
            self.comment = CommentSchema().load(self.data)
        except ValidationError as e:
            return json_response(e.messages, 400)
        return json_response(CommentSchema().dump(self.comment))

    def delete(self, request, *args, **kwargs):
        self.comment.delete()
        return json_response()