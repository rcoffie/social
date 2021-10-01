from django.urls import path
from . import views

app_name = 'social'

urlpatterns = [
    path('',views.Index,name='index'),
    path('edit_post/<int:id>/',views.editPost,name="edit_post"),
    path('delete/<int:id>/',views.deletePost,name="delete_post"),
    path('edit_comment/<int:id>/',views.editComment,name="edit_comment"),
    path('delete/<int:id>/',views.deleteComment,name="delete_comment"),
    path('<int:id>/',views.postDetail,name="post_detail"),
    
]
