from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from blog.models import Blog
from blog.forms import BlogForm


#shows the all posts
def blog_home(request):
    posts = Blog.objects.all() 
    return render(request, 'blog_home.html', {'posts':posts})


#post creation..                                    
@login_required(login_url='/login/')#checks whether user login or not.
def post_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            post_instance = form.save(commit=False)
            post_instance.owner = request.user 
            post_instance.save() 
            return redirect('blog_home')
    else:
        form = BlogForm()
    return render(request,'post_create.html',{'form':form})


#shows the post completely
def post_details(request,pk):
    try:
       post= Blog.objects.get(pk=pk) 
    except Blog.DoesNotExist:
        raise Http404
    return render(request, 'post_details.html', {'post': post})


#Editing
@login_required(login_url='/login/')
def post_update(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if post.owner == request.user:
        form = BlogForm(request.POST or None, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog_home')
    else:
        return redirect('blog_home')
    return render(request, 'post_create.html', {'form':form})


#Deleting
@login_required(login_url='/login/')
def post_delete(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if post.owner == request.user:
        if request.method == 'POST':
            return redirect('blog_home')
    else:
        return redirect('blog_home')
    return render(request, 'post_delete.html', {'post':post})
