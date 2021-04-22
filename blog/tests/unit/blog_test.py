from unittest import TestCase
from blog import blog

class BlogTest(TestCase):
    def test_create_blog(self):
        b = blog.Blog('Test', 'Test Author')

        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([], b.posts)

    def test_repr(self):
        b = blog.Blog('Test', 'Test Author')
        b2 = blog.Blog('My Day', 'Izzyevermore')

        self.assertEqual(b.__repr__(), 'Test by Test Author (0 posts)')
        self.assertEqual(b2.__repr__(), 'My Day by Izzyevermore (0 posts)')

    def test_repr_mutiple_posts(self):
        b = blog.Blog('Test', 'Test Author')
        b.posts = ['test']
        b2 = blog.Blog('My Day', 'Izzyevermore')
        b2.posts = ['test', 'another']

        self.assertEqual(b.__repr__(), 'Test by Test Author (1 post)')
        self.assertEqual(b2.__repr__(), 'My Day by Izzyevermore (2 posts)')