from django import forms
from django.urls import reverse_lazy
from .models import *
from .widget import CountTextInput, AutoCompleteWidget, NaverMapPointWidget, RateitjsWidget

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['name']
        widgets = {
            'name' : CountTextInput,
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'rating': RateitjsWidget,
            'country': AutoCompleteWidget(ajax_url=reverse_lazy('blog:country_list')),
            'location': NaverMapPointWidget,

        }