from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
# Create your views here.
def index(request):
  return HttpResponse('안녕하세요')

def review_list(request):
    reviews = Post.objects.values('title', 'star', 'year', 'genre')
    return render(request, 'movie/review_list.html', {'reviews': reviews})

def create_post(request,pk):
    new_post=Post.objects.get(id=pk)
    if request.method == "POST":
        Post.objects.create(
            title = request.POST['title'],
            year = request.POST['year'],
            genre = request.POST['genre'],
            star = request.POST['star'],
            running_time = request.POST['running_time'],
            text = request.POST['text'],
            pd = request.POST['pd'],
            actors = request.POST['actors']
        )
        return redirect('post_detail', pk=new_post.pk)
    
    return render(request, 'movie/create_post.html')


def post_detail(request, pk):
    review = Post.objects.get(id=pk)
    return render(request, 'movie/post_detail.html', {'review': review})


def review_edit(request, pk):
    review = Post.objects.get(id=pk)
    if request.method == "POST":
        review.title = request.POST['title'],
        review.year = request.POST['year'],
        review.genre = request.POST['genre'],
        review.star = request.POST['star'],
        review.runningtime = request.POST['runningtime'],
        review.text = request.POST['text'],
        review.pd = request.POST['pd'],
        review.actors = request.POST['actors']
        return redirect('review_detail', pk=review.pk)
    return render(request, 'movie/create_post.html',{'review':review})