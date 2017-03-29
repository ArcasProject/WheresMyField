from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers
from library import views

router = routers.DefaultRouter()
router.register(r'article', views.ArticleViewSet)
router.register(r'author', views.AuthorViewSet)
router.register(r'year', views.YearViewSet)
router.register(r'label', views.LabelViewSet)
router.register(r'keyword', views.KeyWordViewSet)
router.register(r'strategies', views.StrategiesViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
