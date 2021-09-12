from django.urls import path
from . import views

app_name = 'social'

urlpatterns = [
    path('',views.Index,name='index'),
    path('<int:id>/',views.postDetail,name="post_detail")
]
