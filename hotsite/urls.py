from django.urls import path
from . import views
from .views import ReportView

urlpatterns = [
   # path("<int:id>", views.Post_listView, name='post_list'),
    #path('', views.HomeView, name= 'home'),
    path('', ReportView.as_view(), name='post_list'),
   #path('', ItemView.as_view(), name='post_list'),
   #path('', views.PodcastView, name='post_list'),
   #path('',views.StorieView, name='post_list')
]
