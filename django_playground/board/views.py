from django.shortcuts import render, redirect
from board.forms import PostForm 

def new_post(request):
    form = PostForm()
    return render(request, 'board/new_post.html', {
        'form' : form,
        })
