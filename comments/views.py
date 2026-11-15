from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import comment_form
from .models import comment_model

@login_required(login_url='login')
def comment_view(request):
    if request.method == 'POST':
        form = comment_form(request.POST , request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)  # stop saving immediately
            comment.user = request.user        # attach logged-in user
            comment.save()
            return redirect('comments')
    else:
        form = comment_form()

    comments = comment_model.objects.all().order_by('-created_at')

    return render(request, 'comment.html', {
        'form': form,
        'comments': comments
    })