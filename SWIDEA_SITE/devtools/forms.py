from django import forms
from devtools.models import DevTool  # DevTool 모델을 올바르게 임포트

class DevToolForm(forms.ModelForm):
    class Meta:
        model = DevTool
        fields = ['name', 'kind', 'content']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '개발 도구 이름'}),
            'kind': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '종류'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '개발 도구 설명'}),
        }
