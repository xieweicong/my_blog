Created by python, flask
        using bootstrap,jQuery, ckeditor, moment 

# How to run

clone the repository
```
$ git clone https://github.com/lottie0914-faye/buildatblog2020.git
$ cd buildatblog2020
```
install packages and create virtual environment:
```
$ pip3 install pipenv
$ pipenv install 
$ pipenv shell
```
initialize admin and run flask
```
$ flask forge
$ flask run
* Running on http://127.0.0.1:5000/
```

Admin account:
* username: `feifei`
* password: `feifeipw`

In order to quit running flask
```
control + c #quit running flask
```

How to run testing file:
```
$ python -m unittest discover -v
```

In order to quit virtual environment 
```
$ exit
```

# Server on cloud:
http://charlie0914.pythonanywhere.com


You can log in with admin account to　create new posts, edit posts and delete posts.

Admin account:
* username: `feifei`
* password: `feifeipw`

### Homepage(list of posts)：

http://charlie0914.pythonanywhere.com/

### Log in:
```
http://charlie0914.pythonanywhere.com/auth/login
```

### Log out:
```
http://charlie0914.pythonanywhere.com/auth/logout
```

### Show single post:
```
http://charlie0914.pythonanywhere.com/post/<int:post_id>
```
### Create new post:
```
http://charlie0914.pythonanywhere.com/admin/post/new
```

### list of posts for manageing:
```
http://charlie0914.pythonanywhere.com/admin/post/manage
```

### edit post:
```
http://charlie0914.pythonanywhere.com/admin/post/<int:post_id>/edit
```

### delete post:
```
http://charlie0914.pythonanywhere.com/admin/post/<int:post_id>/delete
```

## upload file:
```
http://charlie0914.pythonanywhere.com/admin/uploads/<path:filename>
```








