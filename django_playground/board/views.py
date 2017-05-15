from django.shortcuts import render, redirect, get_object_or_404
from .models import SummerNote
from .forms import PostForm

def new_post(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save()
			return redirect(post)
	else:
		form = PostForm()
	return render(request, 'board/new_post.html', {'form' : form,})

def post_detail(request, id):
	post = get_object_or_404(SummerNote, id=id)
	return render(request, 'board/post_detail.html', {
		'post': post,
	})
