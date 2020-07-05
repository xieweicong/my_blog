
from buildatblog.models import Admin, Post
from buildatblog.extensions import db
from tests.base import BaseTestCase


class CLITestCase(BaseTestCase):

    def setUp(self):
        super(CLITestCase, self).setUp()
        db.drop_all()

    def test_initdb_command(self):
        result = self.runner.invoke(args=['initdb'])
        self.assertIn('Initialized database.', result.output)


    def test_forge_command(self):
        result = self.runner.invoke(args=['forge'])

        self.assertEqual(Admin.query.count(), 1)
        self.assertIn('Generating the administrator...', result.output)
