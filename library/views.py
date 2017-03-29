from rest_framework import viewsets
from .serializers import *


class ArticleViewSet(viewsets.ModelViewSet):
    """
    View function for Article objects.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    """
    View function for Author objects.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class YearViewSet(viewsets.ModelViewSet):
    """
    View function for Year objects.
    """
    queryset = Year.objects.all().order_by('year')
    serializer_class = YearSerializer


class LabelViewSet(viewsets.ModelViewSet):
    """
    View function for Label objects.
    """
    queryset = Label.objects.all()
    serializer_class = LabelsSerializer


class KeyWordViewSet(viewsets.ModelViewSet):
    """
    View function for Key word objects.
    """
    queryset = Year.objects.all()
    serializer_class = KeyWordSerializer


class StrategiesViewSet(viewsets.ModelViewSet):
    """
    View function for Strategies objects.
    """
    queryset = Strategies.objects.all()
    serializer_class = StrategiesSerializer
