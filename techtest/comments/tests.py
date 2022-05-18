
# Create your tests here.
import json

from django.test import TestCase
from django.urls import reverse

from .models import Comment
from techtest.movies.models import Movie


class CommentListViewTestCase(TestCase):
    def setUp(self):
        self.movie_url = reverse("movies-list")
        self.Movie_1 = Movie.objects.create(id=2, Title ="this is movie2")
        self.Movie_2 = Movie.objects.create(id=3, Title ="this is movie3")
        self.url = reverse("comment-list")
        self.Comment_1 = Comment.objects.create(id=2, Comments="this is a test comment2")
        self.Comment_2 = Comment.objects.create(id=3, Comments="this is a test comment3")

    def test_serializes_with_correct_data_shape_and_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertCountEqual(
            response.json(),
            [
                {
                    "id": self.Comment_1.id,
                    "Comments":"this is a test comment2"
                    
                },
                {
                    "id": self.Comment_2.id,                 
                    "Comments":"this is a test comment3"
                },
            ],
        )
       
    def test_creates_new_Comment(self):
        movie_payload ={ "title":"fast"}
        response_movie = self.client.post(
            self.movie_url, data=json.dumps(movie_payload), content_type="application/json"
        )
       
        payload = {
            "id" : 4,
            "Comments":"this is a test comment0"
        }
        response = self.client.post(
            self.url, data=json.dumps(payload), content_type="application/json"
        )
        comment = Comment.objects.last()
        self.assertEqual(response.status_code, 201)
        self.assertIsNotNone(comment)
      
        self.assertDictEqual(
            {
                "id": comment.id,                
                "Comments":"this is a test comment0",
            },
            response.json(),
        )
        self.assertEqual(Comment.objects.count(), 3)
        

