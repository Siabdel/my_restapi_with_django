from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User 

from .models import BlogApi 

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(
            username='testuser1', password='abc123')
        testuser1.save()
        
        # create a blog post 
        test_post = BlogApi.objects.create(
            author=testuser1, title='Blog title', body='Body content...')
        test_post.save()
        
    def test_post_content(self):
        post = BlogApi.objects.get(id=1)
        expected_author = f'{post.author}'
        expected_title = f'{post.title}'
        expected_body = f'{post.body}'

        self.assertEqual(expected_author, 'testuser1')
        self.assertEqual(expected_title, 'Blog title')
        self.assertEqual(expected_body, 'Body content...')
        