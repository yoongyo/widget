from django import forms
from .models import Post,Country
from django_summernote.widgets import SummernoteWidget
from .widgets import CounterTextInput, RateitjsWidget, AutoCompleteWidget


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['name']
        widgets = {
            'name': CounterTextInput,
        }



# 첫 번째 방법 : Form Field는 그대로 두고, Widget만 변경하기
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'rating': RateitjsWidget,
            'country': AutoCompleteWidget,
        }

















# 두번재 방법 : Form Field 재정의하면서, Widget 지정하기
"""
class PostForm(forms.ModelForm):
    content = forms.CharField(widget=SummerenoteWidget)   # 기존 폼 Field는 무시
    
    class Meta:
        model = Post
"""

# 세 번째 방법 : 생정사에서 변경하기
"""
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs):
        self.fields['content'].widget = SummernoteWidget()

"""