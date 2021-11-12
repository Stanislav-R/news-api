from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    vote = models.IntegerField(default=0)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def upvote(self):
        self.vote += 1
        self.save(force_update=True)

    class Meta:
        ordering = ["-created"]


class Comment(models.Model):
    author = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"{self.author}'s post"
