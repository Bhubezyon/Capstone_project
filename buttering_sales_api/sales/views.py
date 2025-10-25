from rest_framework.permissions import IsAuthicated
from rest_framework.authentication import TokenAuthentication 
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework import status, generics, permissions
from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer, PostSerializer, CommentSerializer, LikeSerializer

CustomUser = get_user_model()

class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthicated]

    def get_object(self):
        return self.request.user

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class LikeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = Post.objects.get(id=post_id)
        post.likes.add(request.user)
        return Response({'message': 'Post liked'}, status=status.HTTP_200_OK)

class UnlikeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = Post.objects.get(id=post_id)
        post.likes.remove(request.user)
        return Response({'message': 'Post unliked'}, status=status.HTTP_200_OK)

class FollowView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target_user = CustomUser.objects.get(id=user_id)
        if request.user == target_user:
            return Response({'error': 'You cannot follow yourself.'}, status=status.HTTP_400_BAD_REQUEST)
        Follow.objects.get_or_create(follower=request.user, following=target_user)
        return Response({'message': f'You are now following {target_user.username}'}, status=status.HTTP_200_OK)

class UnfollowView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target_user = CustomUser.objects.get(id=user_id)
        follow = Follow.objects.filter(follower=request.user, following=target_user)
        if follow.exists():
            follow.delete()
            return Response({'message': f'You have unfollowed {target_user.username}'}, status=status.HTTP_200_OK)
        return Response({'error': 'You are not following this user.'}, status=status.HTTP_400_BAD_REQUEST)