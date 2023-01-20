from django.urls import path

from app import views

urlpatterns = [

    path('login/', views.MyprojectLoginView.as_view(), name='login_page'),
    path('register/', views.RegisterUserView.as_view(), name='register_page'),
    path('logout/', views.MyProjectLogout.as_view(), name='logout_page'),
    path('home/', views.FileListView.as_view(), name='home'),
    path('file/', views.upload_and_check_file, name='file'),
    ]
