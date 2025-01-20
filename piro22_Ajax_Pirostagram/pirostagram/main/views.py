from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from .models import Post,Comment
from .forms import PostForm
def profile_view(request, username):
    profile = get_object_or_404(Profile, username=username)
    posts = profile.posts.all()
    context = {
        'profile': profile,
        'posts': posts,
    }
    return render(request, 'main/profile.html', context)


def post_list(request):
    posts = Post.objects.all()
    ctx = {
        'posts': posts,
    }
    return render(request, 'main/post_list.html', ctx)


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:post_list')
        else:
            ctx = {
                'form': form,
            }
            return render(request, 'main/post_new.html', ctx)
    elif request.method == 'GET':
        form = PostForm()
        ctx = {
            'form': form,
        }
        return render(request, 'main/post_new.html', ctx)


from django.views.decorators.csrf  import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
@csrf_exempt
def like_post(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        post.like += 1
        post.save()
        return JsonResponse({'likes': post.like})

@csrf_exempt
@login_required
def add_comment(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        content = request.POST.get('content')
        post = get_object_or_404(Post, id=post_id)
        comment = Comment.objects.create(post=post, user=request.user, content=content)
        return JsonResponse({'status': 'success', 'user': comment.user.username, 'content': comment.content})
    return JsonResponse({'status': 'error'})
   
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()
    context = {
        'post': post,
        'comments': comments,
    }
    return render(request, 'main/post_detail.html', context)

def delete_comment(request, comment_id):
    if request.method == 'POST':
        comment = get_object_or_404(Comment, id=comment_id)
        if comment.user == request.user:  # 작성자 본인 확인
            comment.delete()
            return JsonResponse({'status': 'success', 'message': '댓글이 삭제되었습니다.'})
        return JsonResponse({'status': 'error', 'message': '작성자가 아닙니다'})
    return JsonResponse({'status': 'error', 'message': '에러'})