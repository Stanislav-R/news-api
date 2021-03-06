# Test task for DevelopsToday

### Project was deployed to AWS:
http://ec2-3-15-151-255.us-east-2.compute.amazonaws.com/

### Project was documented by Postman:
https://documenter.getpostman.com/view/17380469/UVC8CkjY 

###For local Deploy:

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