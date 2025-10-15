from rest_framework import viewsets, permissions, filters
from .models import Post, Comment
from serializers import PostSerializer, CommentSerializer
from rest_framework.decorators import action
from rest_framework.response import response

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method in permission.SAFE_METHOD or obj.author == request.user

class PostViewSet(viewsets.ModelsViewSet):
    queryset = Post.object.all()
    serializer_class = PostSerializer
    permission_classes = [permission.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']
    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def like(self, request, pk=None):
        post = self.get_object()
        post.likes.add(request.user)
        Notification.objects.create(
            recipient=post.author,
            sender=request.user,
            post=post,
            message=f"{request.user.username} liked your post."
        )

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def like(self, request, pk=None):
        comment = self.get.object()
        comment.likes.add(request.user)
        Notification.objects.create(
            recipient=comment.author,
            sender=request.user,
            comment=comment,
            message=f"{request.user.username} liked your comment."
        )
        return Response({'status': 'comment liked'})

class NotificationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(recipient=self.request.user)       
    
class MessageViewSet(viewsets.Model.ViewSet):
    serializer_class = MessageSerializer
    permissions_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Message.objects.filter(
            models.Q(sender=self.request.user) | models.Q(recipient=self.request.user)
        ).order_by('-timestamp')

    def perfom_create(self, serializer):
        serializer.save(sender=self.request.user)
