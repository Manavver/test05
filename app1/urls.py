
from django.urls import path
from .import views
urlpatterns = [

    path('post_list/',views.post_list),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('data_post/',views.data_post),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

]
