from django import forms

from post.models import Product

class ProductCreateForm(forms.Form):
    title = forms.CharField(max_length=111)
    content = forms.CharField(widget=forms.Textarea())
    image = forms.ImageField(required=False)
    rate = forms.IntegerField(min_value=3,max_value=20)

