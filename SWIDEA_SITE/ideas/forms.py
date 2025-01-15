from django import forms
from ideas.models import Idea
from devtools.models import DevTool  # 개발툴 모델 임포트

class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ['title', 'image', 'content', 'interest', 'devtool']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '아이디어 제목'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '아이디어 내용을 입력하세요'}),
            'interest': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'devtool': forms.Select(attrs={'class': 'form-control'}),
        }
