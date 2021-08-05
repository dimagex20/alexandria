from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class TestViewSet(APIView):
    """docstring for TestViewSet."""

    def __init__(self):
        pass

    def get(self, request, name=None):
        return Response({"name": name, "GET":request.GET})

class FileUploadViewSet(APIView):
    """docstring for FileUploadViewSet."""

    def __init__(self):
        # todo
        pass

    def post(self, request):
        # todo
        return Response({"todo": "todo"})
