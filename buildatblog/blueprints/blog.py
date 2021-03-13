
from flask import render_template, request, current_app, Blueprint
from flask_login import current_user

from buildatblog.models import Post

blog_bp = Blueprint('blog', __name__)


@blog_bp.route('/')
def index():
    per_page = current_app.config['BUILDATBLOG_POST_PER_PAGE']
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(per_page=per_page)
    posts = pagination.items
    return render_template('blog/index.html', pagination=pagination, posts=posts)

@blog_bp.route('/post/<int:post_id>', methods=['GET'])
def show_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('blog/post.html', post=post)