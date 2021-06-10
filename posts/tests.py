from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

# Create your tests here.


class BlogTests(TestCase):
    """
    let's write a basic test for our post model.
    we want to ensure a logged-in can create a 
    post with title and body
    """

    @classmethod
    def setUpTestData(cls):
        # create a user
        testuser1 = User.objects.create_user(username='test1',
                                             password='abcd1234zbcd')
        testuser1.save()

        # create a blog post

        test_post = Post.objects.create(author=testuser1,
                                        title='Blog Test Title',
                                        body='Body Test Contend')
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'

        self.assertEqual(author, 'test1')
        self.assertEqual(title, 'Blog Test Title')
        self.assertEqual(body, 'Body Test Contend')
