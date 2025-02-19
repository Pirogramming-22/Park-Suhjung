from django.shortcuts import render, get_object_or_404,redirect
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import Idea, IdeaStar
from .forms import IdeaForm
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count
import json
# Create your views here.

#def idea_list(request):
   # return render(request, 'ideas/list.html')

#def idea_create(request):
   # return render(request, 'ideas/create.html')

#def idea_update(request, pk):
    #return render(request, 'ideas/update.html', {'pk': pk})

#def idea_delete(request, pk):
  #  return render(request, 'ideas/delete.html', {'pk': pk})




def idea_list(request):
    # 정렬 기준 가져오기
    sort = request.GET.get('sort', 'created_at')  # 기본 정렬은 등록순
    if sort == 'likes':  # 찜하기순
        ideas = Idea.objects.annotate(likes_count=Count('ideastar')).order_by('-likes_count')
    elif sort == 'name':  # 이름순
        ideas = Idea.objects.order_by('title')
    elif sort == 'updated_at':  # 최신순
        ideas = Idea.objects.order_by('-updated_at')
    else:  # 등록순
        ideas = Idea.objects.order_by('-created_at')

    # 현재 사용자의 찜 상태를 계산
    for idea in ideas:
        idea.is_starred = request.user.is_authenticated and IdeaStar.objects.filter(
            idea=idea, user=request.user
        ).exists()
        idea.wishlist=request.user.is_authenticated and IdeaStar.objects.filter(
            idea=idea, user=request.user
        ).exists()
    # 페이지네이션 처리 (4개씩 표시)
    paginator = Paginator(ideas, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'ideas/list.html', {'page_obj': page_obj, 'sort': sort})

def toggle_like(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    star, created = IdeaStar.objects.get_or_create(idea=idea, user=request.user)

    if not created:
        star.delete()  # 이미 찜한 상태면 삭제
        liked = False
    else:
        liked = True

    return JsonResponse({'liked': liked})


def toggle_star(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    
    if request.method == "POST":
        starred, created = IdeaStar.objects.get_or_create(idea=idea, user=request.user)
        if not created:
            starred.delete()
            starred.is_starred = False
        else:
            starred.is_starred = True
       
        return JsonResponse({'is_starred': starred.is_starred})
    
@csrf_exempt
def adjust_interest(request, pk):
    if request.method == "POST":
        try:
            idea = get_object_or_404(Idea, pk=pk)
            body = json.loads(request.body)  # JSON 데이터 파싱
            adjustment = int(body.get("adjustment", 0))  # 조정 값 가져오기
            idea.interest += adjustment  # 관심도 업데이트
            idea.save()  # 변경 사항 저장
            return JsonResponse({"interest": idea.interest})  # 업데이트된 관심도 반환
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)

def idea_create(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('idea_list')  # 아이디어 목록 페이지로 리다이렉트
    else:
        form = IdeaForm()
    return render(request, 'ideas/create.html', {'form': form})


def idea_detail(request, pk): 
    idea = get_object_or_404(Idea, pk=pk)
    is_starred = IdeaStar.objects.filter(idea=idea, user=request.user).exists() 
    return render(request, 'ideas/detail.html', {'idea': idea,'is_starred': is_starred})
def devtool_detail(request, pk):
    devtool = get_object_or_404(DevTool, pk=pk)
    return render(request, 'ideas/devtool_detail.html', {'devtool': devtool,})

def idea_edit(request, pk): 
    idea = get_object_or_404(Idea, pk=pk) 
    if request.method == 'POST': 
        form = IdeaForm(request.POST, request.FILES, instance=idea) 
        if form.is_valid(): 
            form.save() 
            return redirect('idea_detail', pk=idea.pk) 
        else: 
            form = IdeaForm(instance=idea) 
        return render(request, 'ideas/update.html', {'form': form})
    
def idea_delete(request, pk): 
    idea = get_object_or_404(Idea, pk=pk) 
    if request.method == 'POST': 
        idea.delete() 
        return redirect('idea_list') 
    return render(request, 'ideas/delete.html', {'idea': idea})


def toggle_wishlist(request, pk):
    if request.method == 'POST':
        idea = get_object_or_404(Idea, pk=pk)
        idea.wishlist = not idea.wishlist  # 상태 반전
        idea.save()  # 데이터베이스에 저장
        return JsonResponse({'wishlist': idea.wishlist})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def idea_update(request, pk):
    idea = get_object_or_404(Idea, pk=pk)  # 수정할 아이디어 가져오기
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES, instance=idea)
        if form.is_valid():
            form.save()  # 수정 내용 저장
            return redirect('idea_detail', pk=idea.pk)  # 상세 페이지로 이동
    else:
        form = IdeaForm(instance=idea)  # 기존 데이터로 폼 채우기
    return render(request, 'ideas/update.html', {'form': form, 'idea': idea})