from django.contrib import admin
from django.urls import path
from .views import NewsList, NewsDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', NewsList.as_view()),
    path('<int:pk>', NewsDetail.as_view()),

]


