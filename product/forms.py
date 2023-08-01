from django import forms


class ProductCreateForm(forms.Form):
    image = forms.ImageField(required=False)
    title = forms.CharField(max_length=255)
    description = forms.CharField(widget=forms.Textarea())
    rate = forms.FloatField()


class CategoryCreateForm(forms.Form):
    title = forms.CharField(max_length=255)


class ReviewCreateForm(forms.Form):
    comment = forms.CharField(max_length=255)
