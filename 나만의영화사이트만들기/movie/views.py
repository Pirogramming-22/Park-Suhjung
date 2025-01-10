from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
# Create your views here.
def index(request):
  return HttpResponse('안녕하세요')

def review_list2(request):
    reviews = Post.objects.values('title', 'star', 'year', 'genre','pk')
    return render(request, 'movie/review_list2.html', {'reviews': reviews})

def create_post(request):
   
    if request.method == "POST":
        new_post=Post.objects.create(
            title = request.POST['title'],
            year = request.POST['year'],
            genre = request.POST['genre'],
            star = request.POST['star'],
            running_time = request.POST['running_time'],
            text = request.POST['text'],
            pd = request.POST['pd'],
            actors = request.POST['actors']
        )
        return redirect('movie:review_list2')
    
    return render(request, 'movie/create_post.html')


def post_detail(request, pk):
    review = get_object_or_404(Post, pk=pk)
    return render(request, 'movie/post_detail.html', {'review': review})


def review_edit(request, pk):
    review = Post.objects.get(id=pk)
    if request.method == "POST":
        review.title = request.POST['title'],
        review.year = int(request.POST['year']),
        review.genre = request.POST['genre'],
        review.star = int(request.POST['star'][0]),
        review.running_time = request.POST['running_time'],
        review.text = request.POST['text'],
        review.pd = request.POST['pd'],
        review.actors = request.POST['actors']
        review.save()
        
        return redirect('movie:post_detail', pk=review.pk)
    return render(request, 'movie/review_edit.html',{'review':review})

def review_delete(request, pk):

    if request.method == "POST":
        review = Post.objects.get(id=pk)
        review.delete() 
         
    return redirect('movie:review_list2')  