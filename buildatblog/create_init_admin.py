import random

from buildatblog.extensions import db
from buildatblog.models import Admin



def init_admin():
    admin = Admin(
        username='feifei',
        blog_title="feifei's blog",
        name='FEIFEI',
    )
    admin.set_password('feifeipw')
    db.session.add(admin)
    db.session.commit()