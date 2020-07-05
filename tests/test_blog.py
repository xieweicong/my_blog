from flask import url_for

from buildatblog.models import Post
from buildatblog.extensions import db

from tests.base import BaseTestCase


class BlogTestCase(BaseTestCase):

    def setUp(self):
        super(BlogTestCase, self).setUp()
        self.login()

        post = Post(title='testpost', body='testbody')

        db.session.add_all([post])
        db.session.commit()

    def test_index_page(self):
        response = self.client.get('/')
        data = response.get_data(as_text=True)
        self.assertIn('Test', data)
        self.assertIn('testpost', data)

    def test_post_page(self):
        response = self.client.get(url_for('blog.show_post', post_id=1))
        data = response.get_data(as_text=True)
        self.assertIn('testpost', data)


    


   
