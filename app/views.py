from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from app.forms import AuthUserForm, RegisterUserForm, UploadFile
from app.models import User, File
from django.shortcuts import render, redirect

from app.services import check_and_write_result_to_file
from app.tasks import send_all_result_to_mail


def upload_and_check_file(request):
    if request.method == 'POST':
        form = UploadFile(request.POST, request.FILES)
        if form.is_valid():
            file = File()
            file.user_id = request.user
            file.file = form.cleaned_data["file"]
            file.save()
            email = request.user.username
            global operation_number
            check_and_write_result_to_file(str(file.file), email, operation_number)
            operation_number += 1
            return redirect('home')
    else:
        form = UploadFile()
    return render(request, 'html/file.html', {
        'form': form
    })


class FileListView(ListView):
    model = File
    template_name = 'html/home.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['data'] = File.objects.filter(user_id=self.request.user.id)
        return data


class MyprojectLoginView(LoginView):
    template_name = 'html/login.html'
    form_class = AuthUserForm

    def get_success_url(self):
        self.success_url = 'http://127.0.0.1:8000/home/'
        return self.success_url


class RegisterUserView(CreateView):
    model = User
    template_name = 'html/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login_page')
    success_msg = 'Пользователь успешно создан'

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        aut_user = authenticate(username=username, password=password)
        login(self.request, aut_user)
        return form_valid


class MyProjectLogout(LogoutView):
    next_page = reverse_lazy('login_page')


def check_all_files(request):
    checked_files = File.objects.filter(user_id=request.user.id, status='Ждет проверки')
    for i in checked_files:
        i.status = 'Проверяется'
        i.save()
    send_all_result_to_mail.delay()
    try:
        for i in checked_files:
            i.status = 'Готов'
            i.save()
    except:
        for i in checked_files:
            i.status = 'Завершен с ошибкой'
            i.save()
    return redirect('home')
