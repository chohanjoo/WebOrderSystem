from django.shortcuts import render, redirect,resolve_url
from .forms import UserForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.template import RequestContext
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import (
    AuthenticationForm
)   
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            #login(request, new_user)
            return redirect('accounts:login')
    else:
        form = UserForm()
    return render(request, 'accounts/join.html', {'form': form})


# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.save()
#             return redirect('accounts:login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'accounts/join.html',{
#         'form':form,
#     })

# def signin(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return HttpResponse('로그인 성공.')
#         else:
#             return HttpResponse('로그인 실패. 다시 시도 해보세요.')
#     else:
#         form = LoginForm()
#         return render(request, 'accounts/login.html', {'form' : form})

class MyLoginView(LoginView):
    model = User
    form_class = AuthenticationForm
    template_name = 'accounts/login.html'

    def get_success_url(self,user):
        return resolve_url('owner:index',pk=user.pk)

    def form_valid(self,form):
        auth_login(self.request, form.get_user())
        return redirect(self.get_success_url(form.get_user()))

signin = MyLoginView.as_view()

def profile(request,pk):
    user_profile = Profile.objects.get(pk=pk)
    return render(request,'accounts/profile.html',{
        'profile': user_profile,
    })