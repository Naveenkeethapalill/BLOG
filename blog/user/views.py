from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Post
from . forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def index (request):
    post = Post.objects.all()
    return render (request,'index.html', {'post':post})
@login_required
def create(request):
    form=PostForm(request.POST, request.FILES)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'create.html',{'form':form})
def single(request,id):
    blog = Post.objects.get(id=id)
    return render(request,'single.html', {'blog': blog})
@login_required
def delete(request,id):
    blog = Post.objects.get(id=id)
    if request.method == 'POST':
        blog.delete()
        return redirect('index')
@login_required
def edit(request,id):
    blog = Post.objects.get(id=id)
    form = PostForm(instance=blog)
    if request.method == 'POST' :
        form = PostForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render (request,'edit.html',{'form':form})        
def register(request):
    form = UserCreationForm()
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'register.html',{'form':form})
    

