from django.contrib.auth.models import User
from rest_framework import generics, permissions, renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Snippet
from .permissions import IsOwnerOrReadyOnly
from .serializers import SnippetSerializer, UserSerializer


@api_view(['GET'])
def api_root(request, *args, **kwargs):
    return Response({
        'users': reverse('user-list', request=request, *args, **kwargs),
        'snippets': reverse('snippet-list', request=request, *args, **kwargs),
    })


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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadyOnly]


class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
