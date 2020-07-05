from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from flask_login import LoginManager
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
# from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()
ckeditor = CKEditor()
moment = Moment()
# toolbar = DebugToolbarExtension()
migrate = Migrate()


@login_manager.user_loader
def load_user(user_id):
    from buildatblog.models import Admin
    user = Admin.query.get(int(user_id))
    return user
