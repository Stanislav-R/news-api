# Test task for DevelopsToday

###Deploy:

For deployment to your PC use next steps:
1. Clone repo: https://github.com/Stanislav-R/news-api.git
2. Create virtualenv and activate it:
   - python3 -m venv venv
   - venv/bin/activate
3. Install Docker
4. Run in terminal docker-compose up --build
5. Make migration: 
   - python manage.py makemigrations
   - python manage.py migrate
7. Application will be available at: http://127.0.0.1:8000/

###Available api's:

http://127.0.0.1:8000

| API                           | Action                              |
|-------------------------------|-------------------------------------|
| /posts/                       | Show all posts, Create a post       |
| /comments/                    | Show all comments, Create a comment |
| /posts/<int: post_id>/        | CRUD for a post with id             |
| /comments/<int: comment_id>/  | CRUD for a comment with id          |
| /posts/<int: post_id>/upvote/ | Endpoint to upvote the post         |

###Code formatted with:
1. Back
2. Flake8