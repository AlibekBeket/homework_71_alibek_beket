from django import forms

from instagram.models import Posts, Comments


class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('description', 'img')

    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get('description')
        if len(description) < 3:
            raise forms.ValidationError('Количество символов должно быть больше 2 символов')


class SearchForm(forms.Form):
    search = forms.CharField(
        max_length=200,
        required=False,
        label='Найти'
    )


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('description',)

    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get('description')
        if len(description) < 3:
            raise forms.ValidationError('Количество символов должно быть больше 2 символов')