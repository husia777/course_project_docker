from django.urls import path, include
from django.views.generic import TemplateView
from app import views
from app.tasks import send_all_result_to_mail

urlpatterns = [
     path('login/', views.MyprojectLoginView.as_view(), name='login_page'),
    path('', include('django.contrib.auth.urls')),
    # path('login/', views.MyprojectLoginView.as_view(), name='login_page'),
    path('register/', views.RegisterUserView.as_view(), name='register_page'),
    path('logout/', views.MyProjectLogout.as_view(), name='logout_page'),
    path('home/', views.FileListView.as_view(), name='home'),
    path('file/', views.upload_and_check_file, name='file'),
    path('upload/all/', views.check_all_files, name='all'),
    path('verify_email/<uidb64>/<token>/', views.EmailVerify.as_view(), name='verify_email'),
    path('invalid_verify/', TemplateView.as_view(template_name='html/invalid_verify.html'), name='invalid_verify'),
    path('confirm_email/', TemplateView.as_view(template_name='html/confirm_email.html'), name='confirm_email')
    ]
