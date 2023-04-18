from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
path('malli', admin.site.urls),
path('',views.indexpage,name='indexpage'),
path('delete/<int:myid>',views.delete,name='delete'),
path('edit/<int:myid>',views.edit,name='edit'),
]
