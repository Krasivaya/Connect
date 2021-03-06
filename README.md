# Connect

### Developed By
[Carine I. SEMWAGA](https://github.com/Krasivaya)

## Description
This is an idea sharing platform, which help users to express their thoughts through creation of articles and sharing the articles with their networks. An author can create a post, and then, other users can react to the posts.

## API Information

|   Method   |   Description   |   Endpoint  |
|  -------   |   ---   |   ---   |
|   GET    |   A user can view all article posts  |   localhost:8000  |
|   GET |   A user can view a single article post  |   localhost:8000/article/:postId   |
|   POST  |   A user can comment on an article post  |   localhost:8000/article |
|  POST |   A user can like an article post  |   localhost:8000  |
| POST    |   A user can share an article post  |   localhost:8000/article/shared  |
|   GET    |   A user can view recent posts   |   localhost:8000/    |
|   POST   |   A user can get an email alert once a new article post is made  |   localhost:8000 |
|   POST  |   An author can sign up  |   localhost:8000/auth/signup   |
| POST    |   An author can login  |   localhost:8000/auth/signin    |
|   POST    |   An author can create a post    |   localhost:8000/article    |
|   DELETE   |   An author can delete comments  |   localhost:8000/article/:cmId |
|   DELETE    |   An author can delete a post  |   localhost:8000/article/:postId    |
|   UPDATE    |   An author can update a post  |   localhost:8000/article/:postId    |
|   GET    |   An admin can view all authors    |   localhost:8000/admin/authors    |
|   GET    |   An admin can view all article posts    |   localhost:8000/admin/posts    |
|   GET    |   An admin can view all comments    |   localhost:8000/admin/comments    |
|   DELETE    |   An admin can delete comments    |   localhost:8000/admin/comments/:cmId    |
|   DELETE    |   An admin can delete posts    |   localhost:8000/admin/posts/:postId    |


## Technologies Used

1. Python3.6
2. Env
3. Django 
4. Postgresql
5. HTML5 & CSS
6. Bootsrap & jQuery
7. Git Version Control 

## Setup/Installation Requirements

* Open your terminal
* initialize github, git clone ` https://github.com/Krasivaya/Connect.git `
* cd Connect
* open folder in prefered IDE
* open terminal
* Activate Env `source virtual/bin/activate`
* Install the latest version of pip `curl https://bootstrap.pypa.io/get-pip.py | python`
* Install all requirements `pip install -r requirements.txt`
* Run in terminal `chmod a+x start.sh`
* Run in terminal `./start.sh`
* Run the application in your localhost provided

## Known Bugs
No bug known. If you found any, please contact!

## License
This project is under the [MIT](https://github.com/Krasivaya/Connect/blob/master/LICENSE) license.

##### Copyright © 2020 Carine I. SEMWAGA.
