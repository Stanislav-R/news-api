from apscheduler.schedulers.background import BackgroundScheduler

from .models import Post

scheduler = BackgroundScheduler()
job = None


def reset_count_votes():
    posts = Post.objects.all()
    posts.update(vote=0)


def start_job():
    global job
    job = scheduler.add_job(reset_count_votes, "interval", hours=24)
    scheduler.start()
