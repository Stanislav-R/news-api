from rest_framework import viewsets, views, generics
from rest_framework.response import Response

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class UpvoteView(views.APIView):
    def get(self, pk):
        post = generics.get_object_or_404(Post, pk)
        post.upvote()

        return Response({"message": f"Post #{pk} has been upvote"})
