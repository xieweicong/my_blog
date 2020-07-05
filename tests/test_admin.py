from flask import url_for

from buildatblog.models import Post
from buildatblog.extensions import db

from tests.base import BaseTestCase


class AdminTestCase(BaseTestCase):

    def setUp(self):
        super(AdminTestCase, self).setUp()
        self.login()
        post = Post(title='Testtitle', body='Testbody')
        db.session.add_all([post])
        db.session.commit()

    def test_new_post(self):
        response = self.client.get(url_for('admin.new_post'))
        data = response.get_data(as_text=True)
        self.assertIn('New Post', data)

        response = self.client.post(url_for('admin.new_post'), data=dict(
            title='testnewpost',
            body='testnewbody'
        ), follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertIn('Post created.', data)
        self.assertIn('testnewpost', data)
        self.assertIn('testnewbody', data)


    def test_delete_post(self):
        response = self.client.get(url_for('admin.delete_post', post_id=1), follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertNotIn('Post deleted.', data)
        self.assertIn('405 Method Not Allowed', data)

        response = self.client.post(url_for('admin.delete_post', post_id=1), follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertIn('Post deleted.', data)

    