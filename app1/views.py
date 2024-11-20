from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm

from .models import Post


# Create your views here.

def post_list(request):
    p=Post.objects.all()
    return render(request,'post_list.html',{'p':p})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def data_post(request):
    if request.method=="POST":
        A=Post()
        A.title=request.POST['name']
        A.text=request.POST['details']

        A.save()
        #return render(request, 'post.html')
        return redirect('/app1/post_list/')
    else:
        return render(request, 'post.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/app1/post_list/')  # Change to your home URL
    else:
        form = SignUpForm()

    return render(request, 'app1/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/app1/post_list/')  # Change to your home URL
        else:
            return render(request, 'app1/login.html', {'error': 'Invalid login'})
    return render(request, 'app1/login.html')

def user_logout(request):
    logout(request)
    return redirect('/app1/login/')