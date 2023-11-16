from django.contrib import admin
from django.urls import path

from post.views import hello_view
from post.views import date_view
from post.views import by_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_view),
    path('current_date/', date_view),
    path('goodby/', by_view)

]
