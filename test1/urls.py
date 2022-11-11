from django.contrib import admin
from django.urls import path,include
from .views import ListPersonview
urlpatterns = [
    path('b/',ListPersonview.as_view() ),
    path('<int:khoa_chinh>',ListPersonview.as_view())

]