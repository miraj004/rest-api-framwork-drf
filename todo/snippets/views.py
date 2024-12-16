

# TODO Function based request handling
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer


# @api_view(['GET', 'POST'])
# def snippet_list(request, format=None):
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# @api_view(['GET', 'PUT', 'DELETE'])
# def snippet_detail(request, pk, format=None):
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# TODO class based request handling

# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status


# class SnippetList(APIView):

#     def get(self, request, format=None):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


# class SnippetDetail(APIView):
    
#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


#TODO USING MIXIN CLASSES

# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer
# from rest_framework import mixins
# from rest_framework import generics

# class SnippetList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class SnippetDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# TODO USING GENERIC CLASS BASED

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework import generics, permissions
from snippets.permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User

# ROOT API IMPORTS
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
# FOR RENDERERS
from rest_framework import renderers


# FOR VIEWSET

from rest_framework import viewsets
from rest_framework.decorators import action


# Becauase of using defaut router in urls.py there is no longer need to the following api root function.
# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'users': reverse('user-list', request=request, format=format),
#         'snippets': reverse('snippet-list', request=request, format=format)
#     })

# END API ROOT

# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# TODO USINV VIEW SET MERGE UserList <-> UserDetail with on ViewSet




class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

# TODO END USINV VIEW SET MERGE UserList <-> UserDetail with on ViewSet





#TODO

# class SnippetList(generics.ListCreateAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)


# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


# class SnippetHighlight(generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     renderer_classes = [renderers.StaticHTMLRenderer]

#     def get(self, request, *args, **kwargs):
#         snippet = self.get_object()
#         return Response(snippet.highlighted)

# TODO REPLACING above three snippets classes with ono view set
class SnippetViewSet(viewsets.ModelViewSet):
    
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# END TODO 
