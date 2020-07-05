How to run

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

Server on cloud:
http://lottie0914.pythonanywhere.com


You can log in with admin account to　create new posts, edit posts and delete posts.

Admin account:
* username: `feifei`
* password: `feifeipw`
