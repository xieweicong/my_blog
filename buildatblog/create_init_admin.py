import random

from buildatblog.extensions import db
from buildatblog.models import Admin



def init_admin():
    admin = Admin(
        username='xieweicong',
        blog_title="",
        name='XIEWEICONG',
    )
    admin.set_password('xieweicong95')
    db.session.add(admin)
    db.session.commit()