from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions

from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer


class SnippetList(generics.ListCreateAPIView):
    """
    List snippets or create a new one
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    # ensure that authenticated requests get read-write access,
    # and unauthenticated requests get read-only access
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View, update or delete one snippet by its primary key
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    # ensure that authenticated requests get read-write access,
    # and unauthenticated requests get read-only access
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
