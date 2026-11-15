from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

# Create your views here.
@login_required(login_url='login')
def postView(request):
    if request.method == 'POST':
        form = postForm(request.POST , request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            form = postForm()
    else:
        form = postForm()
    posts = postModel.objects.all().order_by('heading')
    return render(request , 'post.html' ,{'form':form , 'posts':posts})


@login_required(login_url='login')
def editView(request , pk):
    post = get_object_or_404(postModel , pk=pk)
    if request.method == "POST":
        form = postForm(request.POST ,request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts')
    else:
        form = postForm(instance=post)

    return render(request,'edit.html' ,{'form':form})

@login_required(login_url='login')
def deleteView(request, pk):
    post = get_object_or_404(postModel, pk=pk)

    if request.method == 'POST':
        post.delete()

    return redirect('posts')
